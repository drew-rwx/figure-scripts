#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.colors as colors
import numpy as np

def read_my_file(file):
    with open(file, "r") as fin:
        data = fin.read()
        return data
#
# Parameter Search
# 
data = read_my_file("data/generations_search.txt")
data = data.splitlines()

x_vals = [int(x) for x in data[0].split()]
y_vals = [float(x) for x in data[1].split()]

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']
fig, ax = plt.subplots(figsize=(3,3))
ax.plot(x_vals, y_vals, linewidth=2.0)
# ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
# ax.set_xticks([float(x) for x in range(0, 551, 50)])
ax.set_yticks([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
ax.tick_params(axis='both', labelsize=11)
# ax.tick_params(axis='y', length=0)
ax.set_xlabel("Generations", fontsize=12)
ax.set_ylabel("Compression Ratio", fontsize=12)
# ax.set_title(ds_title, fontsize=13)
ax.set_axisbelow(True)
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

plt.xlim(0, 200)
plt.tight_layout()
# plt.show()
plt.savefig(f'figs/search_gen.pdf')

data = read_my_file("data/population_search.txt")
data = data.splitlines()

x_vals = [int(x) for x in data[0].split()]
y_vals = [float(x) for x in data[1].split()]
print(*x_vals)
print(*y_vals)


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']
fig, ax = plt.subplots(figsize=(3,3))
ax.plot(x_vals, y_vals, linewidth=2.0)
# ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
# ax.set_xticks([float(x) for x in range(0, 551, 50)])
ax.set_yticks([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
ax.tick_params(axis='both', labelsize=11)
# ax.tick_params(axis='y', length=0)
ax.set_xlabel("Population Size", fontsize=12)
ax.set_ylabel("Compression Ratio", fontsize=12)
# ax.set_title(ds_title, fontsize=13)
ax.set_axisbelow(True)
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

plt.xlim(1, 50)
plt.tight_layout()
plt.savefig(f'figs/search_pop.pdf')

data = read_my_file("data/mr_search.txt")
data = data.splitlines()

x_vals = [float(x) for x in data[0].split()]
y_vals = [float(x) for x in data[1].split()]
print(*x_vals)
print(*y_vals)


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif']
fig, ax = plt.subplots(figsize=(3,3))
ax.plot(x_vals, y_vals, linewidth=2.0)
# ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
# ax.set_xticks([float(x) for x in range(0, 551, 50)])
ax.set_yticks([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
ax.tick_params(axis='both', labelsize=11)
# ax.tick_params(axis='y', length=0)
ax.set_xlabel("Mutation Rate", fontsize=12)
ax.set_ylabel("Compression Ratio", fontsize=12)
# ax.set_title(ds_title, fontsize=13)
ax.set_axisbelow(True)
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

plt.xlim(0.0, 1.0)
plt.tight_layout()
# plt.show()
plt.savefig(f'figs/search_mr.pdf')

print("psearch done")
print()

#
# C + S Throughput
#
data = read_my_file("data/comp_search_throughput.csv")
data = data.splitlines()

header = data.pop(0)
header = header.split(',')

datasets = header[1:]
datasets.pop()
datasets = [s.split()[0].strip() for s in datasets]
datasets.append("All Datasets")
print(datasets)

for ds_idx in range(1, len(datasets) + 1):
    compressor_ratio_pair = []
    ds_title = datasets[ds_idx - 1]

    # get data
    for l in data:
        ldata = l.split(',')
        compressor_ratio_pair.append((ldata[0], float(ldata[ds_idx])))

    # sort and remove
    compressor_ratio_pair.sort(key=lambda x: x[1], reverse=False) # best compressors at the end
    # compressor_ratio_pair = compressor_ratio_pair[0:2] + compressor_ratio_pair[-5:] # bottom 2 and top 5
    print(ds_title)
    print(*compressor_ratio_pair, sep='\n')

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['CMU Serif']
    fig, ax = plt.subplots(figsize=(5,5))

    compressor_labels = [x[0] for x in compressor_ratio_pair]
    compressor_ratio = [x[1] for x in compressor_ratio_pair]
    y_position = np.arange(len(compressor_labels))
    y_position = [ y / 3 for y in y_position]

    ax.barh(y_position, compressor_ratio, height=0.2, zorder=1)
    ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
    ax.set_xticks([float(x) for x in range(0, 551, 50)])
    ax.tick_params(axis='x', labelsize=11)
    ax.tick_params(axis='y', length=0)
    ax.set_xlabel("Compression Throughput (GB/s)", fontsize=12)
    # ax.set_title(ds_title, fontsize=13)
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

    plt.xlim(0.0, 550.0)
    plt.tight_layout()
    # plt.show()
    plt.savefig(f'figs/cst_{ds_title}.pdf')
    print()
print("C+S done")
print()

#
# D Throughput
#
data = read_my_file("data/decomp_throughput.csv")
data = data.splitlines()

header = data.pop(0)
header = header.split(',')

datasets = header[1:]
datasets.pop()
datasets = [s.split()[0].strip() for s in datasets]
datasets.append("All Datasets")

for ds_idx in range(1, len(datasets) + 1):
    compressor_ratio_pair = []
    ds_title = datasets[ds_idx - 1]

    # get data
    for l in data:
        ldata = l.split(',')
        compressor_ratio_pair.append((ldata[0], float(ldata[ds_idx])))

    # sort and remove
    compressor_ratio_pair.sort(key=lambda x: x[1], reverse=False) # best compressors at the end
    # compressor_ratio_pair = compressor_ratio_pair[0:2] + compressor_ratio_pair[-5:] # bottom 2 and top 5
    print(ds_title)
    print(*compressor_ratio_pair, sep='\n')

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['CMU Serif']
    fig, ax = plt.subplots(figsize=(5,5))

    compressor_labels = [x[0] for x in compressor_ratio_pair]
    compressor_ratio = [x[1] for x in compressor_ratio_pair]
    y_position = np.arange(len(compressor_labels))
    y_position = [ y / 3 for y in y_position]

    ax.barh(y_position, compressor_ratio, height=0.2, zorder=1)
    ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
    ax.set_xticks([float(x) for x in range(0, 551, 50)])
    ax.tick_params(axis='x', labelsize=11)
    ax.tick_params(axis='y', length=0)
    ax.set_xlabel("Decompression Throughput (GB/s)", fontsize=12)
    # ax.set_title(ds_title, fontsize=13)
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

    plt.xlim(0.0, 550.0)
    plt.tight_layout()
    # plt.show()
    plt.savefig(f'figs/dt_{ds_title}.pdf')
    print()
print("D done")
print()

#
# C Throughput
#
data = read_my_file("data/comp_throughput.csv")
data = data.splitlines()

header = data.pop(0)
header = header.split(',')

datasets = header[1:]
datasets.pop()
datasets = [s.split()[0].strip() for s in datasets]
datasets.append("All Datasets")

for ds_idx in range(1, len(datasets) + 1):
    compressor_ratio_pair = []
    ds_title = datasets[ds_idx - 1]

    # get data
    for l in data:
        ldata = l.split(',')
        compressor_ratio_pair.append((ldata[0], float(ldata[ds_idx])))

    # sort and remove
    compressor_ratio_pair.sort(key=lambda x: x[1], reverse=False) # best compressors at the end
    # compressor_ratio_pair = compressor_ratio_pair[0:2] + compressor_ratio_pair[-5:] # bottom 2 and top 5
    print(ds_title)
    print(*compressor_ratio_pair, sep='\n')

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['CMU Serif']
    fig, ax = plt.subplots(figsize=(5,5))

    compressor_labels = [x[0] for x in compressor_ratio_pair]
    compressor_ratio = [x[1] for x in compressor_ratio_pair]
    y_position = np.arange(len(compressor_labels))
    y_position = [ y / 3 for y in y_position]

    ax.barh(y_position, compressor_ratio, height=0.2, zorder=1)
    ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
    ax.set_xticks([float(x) for x in range(0, 551, 50)])
    ax.tick_params(axis='x', labelsize=11)
    ax.tick_params(axis='y', length=0)
    ax.set_xlabel("Compression Throughput (GB/s)", fontsize=12)
    # ax.set_title(ds_title, fontsize=13)
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

    plt.xlim(0.0, 550.0)
    plt.tight_layout()
    # plt.show()
    plt.savefig(f'figs/ct_{ds_title}.pdf')
    print()
print("C done")
print()
#
# Compression Ratio
#
data = read_my_file("data/compression_ratio.csv")
data = data.splitlines()

header = data.pop(0)
header = header.split(',')

datasets = header[1:]
datasets.pop()
datasets = [s.split()[0].strip() for s in datasets]
datasets.append("All Datasets")

for ds_idx in range(1, len(datasets) + 1):
    compressor_ratio_pair = []
    ds_title = datasets[ds_idx - 1]

    # get data
    for l in data:
        ldata = l.split(',')
        compressor_ratio_pair.append((ldata[0], float(ldata[ds_idx])))

    # sort and remove
    compressor_ratio_pair.sort(key=lambda x: x[1], reverse=False) # best compressors at the end
    if ds_idx != (len(datasets)):
        compressor_ratio_pair = compressor_ratio_pair[0:2] + compressor_ratio_pair[-5:] # bottom 2 and top 5
    else:
        pass
    print(ds_title)
    print(*compressor_ratio_pair, sep='\n')

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['CMU Serif']

    if ds_idx != (len(datasets)):
        compressor_ratio_pair = compressor_ratio_pair[0:2] + compressor_ratio_pair[-5:] # bottom 2 and top 5
        fig, ax = plt.subplots(figsize=(5,2.5))
    else:
        fig, ax = plt.subplots(figsize=(5,5))

    compressor_labels = [x[0] for x in compressor_ratio_pair]
    compressor_ratio = [x[1] for x in compressor_ratio_pair]
    y_position = np.arange(len(compressor_labels))
    y_position = [ y / 3 for y in y_position]

    if ds_idx != (len(datasets)):
        spacing = 0.2
        y_position[-1] += spacing
        y_position[-2] += spacing
        y_position[-3] += spacing
        y_position[-4] += spacing
        y_position[-5] += spacing
    else:
        pass

    ax.barh(y_position, compressor_ratio, height=0.2, zorder=1)
    ax.set_yticks(y_position, labels=compressor_labels, fontsize=11)
    ax.set_xticks([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0])
    ax.tick_params(axis='x', labelsize=11)
    ax.tick_params(axis='y', length=0)
    ax.set_xlabel("Compression Ratio", fontsize=12)
    # ax.set_title(ds_title, fontsize=13)
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, zorder=0)

    if ds_idx != (len(datasets)):
        compressor_ratio_pair = compressor_ratio_pair[0:2] + compressor_ratio_pair[-5:] # bottom 2 and top 5
        plt.xlim(1.0, 2.0)
        fig.add_artist(lines.Line2D([0.205,0.95],[0.454, 0.454], color='k', linestyle='--', linewidth=0.5))
    else:
        plt.xlim(1.0, 1.6)

    plt.tight_layout()
    # plt.show()
    # quit()
    plt.savefig(f'figs/cr_{ds_title}.pdf')
    print()
print("CR done")
print()

