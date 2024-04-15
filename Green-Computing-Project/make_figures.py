#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import statistics

# constants
RUNS = 9
MAX_THREADS = 16

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

data = read_my_file("results.txt")
data = data.splitlines()
current_line = 0

# original
og_rt_list = []
og_eg_list = []

current_line += 1 # skip title
for _ in range(RUNS):
    line = data[current_line]

    rt, _, eg = line.partition(",")

    og_rt_list.append(float(rt))
    og_eg_list.append(float(eg))

    current_line += 1

og_runtime = statistics.mean(og_rt_list)
og_energy = statistics.mean(og_eg_list)

print(f"Original Runtime (s): {og_runtime:.2f}")
print(f"Original Energy (Ws): {og_energy:.2f}")

# efficienet
ef_rt_list = []
ef_eg_list = []

current_line += 1 # skip title
for _ in range(RUNS):
    line = data[current_line]

    rt, _, eg = line.partition(",")

    ef_rt_list.append(float(rt))
    ef_eg_list.append(float(eg))

    current_line += 1

ef_runtime = statistics.mean(ef_rt_list)
ef_energy = statistics.mean(ef_eg_list)

print(f"Efficient Runtime (s): {ef_runtime:.2f}")
print(f"Efficient Energy (Ws): {ef_energy:.2f}")

# number of threads

thd_count = [x for x in range(1, MAX_THREADS + 1)]
thd_runtime = []
thd_energy = []

for _ in range(MAX_THREADS):
    rt_list = []
    eg_list = []

    current_line += 1 # skip title
    for _ in range(RUNS):
        line = data[current_line]

        rt, _, eg = line.partition(",")

        rt_list.append(float(rt))
        eg_list.append(float(eg))

        current_line += 1

    thd_runtime.append(statistics.mean(rt_list))
    thd_energy.append(statistics.mean(eg_list))

print("Thread count:", *thd_count)
print("Runtime: ", end='')
for i in range(len(thd_count)):
    print(f"{thd_runtime[i]:.2f}", end=' ')
print()
print("Energy: ", end='')
for i in range(len(thd_count)):
    print(f"{thd_energy[i]:.2f}", end=' ')
print()

#
# make figures
#

SHOW_FIGURES = True

# runtime

# set font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']

fig, ax = plt.subplots(figsize=(5, 5))

ax.bar(1, og_runtime, 0.2, label='Original', color='blue')
ax.bar(0.6, ef_runtime, 0.2, label='Efficient (8 Threads)', color='red')

# plt.xticks(x + width / 2, ['4 Proc.', '8 Proc.', '12 Proc.', '16 Proc.'])
plt.yticks(np.arange(0, 7.1, 0.5))

ax.set_xlabel("Program Version", fontsize=12)
ax.set_ylabel("Runtime (s)", fontsize=12)

# y: size of numbers, x: remove ticks
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', length=0, labelsize=0)

# legend
ax.legend()

# grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
if SHOW_FIGURES:
    plt.show(block=False)
plt.savefig("runtime.pdf")


# energy

# set font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']

fig, ax = plt.subplots(figsize=(5, 5))

ax.bar(1, og_energy, 0.2, label='Original', color='blue')
ax.bar(0.6, ef_energy, 0.2, label='Efficient (8 Threads)', color='red')

# plt.xticks(x + width / 2, ['4 Proc.', '8 Proc.', '12 Proc.', '16 Proc.'])
plt.yticks(np.arange(0, 161, 10))

ax.set_xlabel("Program Version", fontsize=12)
ax.set_ylabel("Energy (Ws)", fontsize=12)

# y: size of numbers, x: remove ticks
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', length=0, labelsize=0)

# legend
ax.legend()

# grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
if SHOW_FIGURES:
    plt.show(block=False)
plt.savefig("energy.pdf")


# thread runtime

# set font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']

fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(thd_count, thd_runtime, 0.2, color='black', marker='.')

plt.xticks(np.arange(1, MAX_THREADS+1, 1))
plt.yticks(np.arange(0, 7.1, 0.5))

plt.xlim(0.5, MAX_THREADS + 0.5)
plt.ylim(0, 7)

ax.set_xlabel("Number of Threads", fontsize=12)
ax.set_ylabel("Runtime (s)", fontsize=12)

# y: size of numbers, x: remove ticks
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', length=0)

# legend
# ax.legend()

# grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
if SHOW_FIGURES:
    plt.show(block=False)
plt.savefig("thd-runtime.pdf")


# thread energy

# set font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']

fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(thd_count, thd_energy, 0.2, color='black', marker='.')

plt.xticks(np.arange(1, MAX_THREADS+1, 1))
plt.yticks(np.arange(0, 161, 10))

plt.xlim(0.5, MAX_THREADS + 0.5)
plt.ylim(0, 160)

ax.set_xlabel("Number of Threads", fontsize=12)
ax.set_ylabel("Energy (Ws)", fontsize=12)

# y: size of numbers, x: remove ticks
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', length=0)

# legend
# ax.legend()

# grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
if SHOW_FIGURES:
    plt.show(block=False)
plt.savefig("thd-energy.pdf")


# wait for input to show the figures
if SHOW_FIGURES:
    input()
