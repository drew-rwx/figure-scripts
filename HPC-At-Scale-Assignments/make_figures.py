#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import statistics

# constants
X_SECONDS = 60
RUNS = 5
GROUPS = 4

def read_my_file(file):
    with open(file, "r") as fin:
        data = fin.read()
        return data

def write_my_file(file, data):
    # make data writable
    write_data = []
    for d in data:
        write_data.append(str(d) + "\n")

    # write the data
    with open(file, "w") as fout:
        fout.writelines(write_data)

data = read_my_file("data2.txt")
pc_str_data, _, wp_str_data = data.partition("~~~")
pc_str_data = pc_str_data.strip()
wp_str_data = wp_str_data.strip()

pc_str_data = pc_str_data.split("\n\n")
wp_str_data = wp_str_data.split("\n\n")

pc_data = []
for e in pc_str_data:
    e = e.splitlines()
    e.pop(0)
    e.pop()

    entry = []
    for line in e:
        tokens = line.split()
        consumed = int(tokens[-1])
        entry.append(consumed)

    pc_data.append(entry)

wp_data = []
for e in wp_str_data:
    e = e.splitlines()
    e.pop(0)
    e.pop()

    entry = []
    for line in e:
        tokens = line.split()
        consumed = int(tokens[-1])
        entry.append(consumed)

    wp_data.append(entry)

pc_avg = []
pc_low = []
pc_high = []

wp_avg = []
wp_low = []
wp_high = []

# 1000 -- kilo
# 1000 * 1000 -- mega
# 1000 * 1000 * 1000 -- giga
throughput_divisor = 1000

for e in pc_data:
    e = [ elem / X_SECONDS / throughput_divisor for elem in e]
    pc_avg.append(statistics.mean(e))
    pc_low.append(min(e))
    pc_high.append(max(e))

for e in wp_data:
    e = [ elem / X_SECONDS / throughput_divisor for elem in e]
    wp_avg.append(statistics.mean(e))
    wp_low.append(min(e))
    wp_high.append(max(e))


print("Producer-Consumer")
for proc, avg, low, high in zip([4, 8, 12, 16], pc_avg, pc_low, pc_high):
    print(f'{proc} processes:\t{avg=:.2f}\t{low=:.2f}\t{high=:.2f}')
print("~")

print("Work Pool")
for proc, avg, low, high in zip([4, 8, 12, 16], wp_avg, wp_low, wp_high):
    print(f'{proc} processes:\t{avg=:.2f}\t{low=:.2f}\t{high=:.2f}')
print("~")

print("Latex Table")
for proc, pcavg, pclow, pchigh, wpavg, wplow, wphigh in zip([4, 8, 12, 16], pc_avg, pc_low, pc_high, wp_avg, wp_low, wp_high):
    print(f'{proc} & {pcavg:.2f} & {pclow:.2f} & {pchigh:.2f} & {wphigh:.2f} & {wphigh:.2f} & {wphigh:.2f} \\\\ \\hline')
print("~")

print("Comparisons")
for proc, pcavg, wpavg in zip([4, 8, 12, 16], pc_avg, wp_avg):
    times = wpavg / pcavg
    print(f'{proc} processes:\t{times:.2f}')
print("~")

print("PC Scaling")
baseline = pc_avg[0]
for proc, avg in zip([4, 8, 12, 16], pc_avg):
    times = avg / baseline
    print(f'{proc} processes:\t{times:.2f}')
print("~")

print("WP Scaling")
baseline = wp_avg[0]
for proc, avg in zip([4, 8, 12, 16], wp_avg):
    times = avg / baseline
    print(f'{proc} processes:\t{times:.2f}')
print("~")

pc_low = [ (avg - low) for avg, low in zip(pc_avg, pc_low)]
pc_high = [ (high - avg) for avg, high in zip(pc_avg, pc_high)]
wp_low = [ (avg - low) for avg, low in zip(wp_avg, wp_low)]
wp_high = [ (high - avg) for avg, high in zip(wp_avg, wp_high)]


#
# make figures
#

# set font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']

fig, ax = plt.subplots(figsize=(5, 5))

x = np.arange(GROUPS)
width = 0.2

ax.bar(x, pc_avg, width, label='Producer-Consumer', color='blue', yerr=[pc_low, pc_high], capsize=10)
ax.bar(x + width, wp_avg, width, label='Work Pool', color='red', yerr=[wp_low, wp_high], capsize=10)

plt.xticks(x + width / 2, ['4 Proc.', '8 Proc.', '12 Proc.', '16 Proc.'])
plt.yticks(np.arange(0, 8001, 500))

ax.set_xlabel("Number of Processes", fontsize=12)
ax.set_ylabel("Message Throughput (KM/s)", fontsize=12)

# y: size of numbers, x: remove ticks
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', length=0)

# legend
ax.legend(title='Execution Models')

# grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)



plt.tight_layout()
# plt.show()
plt.savefig("throughput.pdf")
