#! /usr/bin/python

import os
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')

font = {'family' : 'serif',
        'size'   : 14}

mpl.rc('font', **font)

d1_path       = "inst_2_para_16_time_900/"
d1_data       = []

d2_path       = "inst_2_para_128_time_900/"
d2_data       = []

d3_path       = "inst_2_para_256_time_900/"
d3_data       = []

d4_path       = "inst_4_para_32_time_900/"
d4_data       = []

d5_path       = "inst_4_para_256_time_900/"
d5_data       = []

d6_path       = "inst_4_para_512_time_900/"
d6_data       = []

d7_path       = "../pla85900_VM/"
d7_data       = []

d8_path       = "../pla85900_HAL14k_seq/"
d8_data       = []

for run in os.listdir(d1_path):
    with open(d1_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d1_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d2_path):
    with open(d2_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d2_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d3_path):
    with open(d3_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d3_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d4_path):
    with open(d4_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d4_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d5_path):
    with open(d5_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d5_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d6_path):
    with open(d6_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d6_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d7_path):
    with open(d7_path + run + "/best.txt") as file:
        best = file.read().splitlines()
        d7_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d8_path):
    with open(d8_path + run + "/best.txt") as file:
        best = file.read().splitlines()
        d8_data.append(float(best[-1].split(" ")[1]))

boxplot_data = [d1_data, d2_data, d3_data,
                d4_data, d5_data, d6_data,
                d7_data, d8_data]

fig = plt.figure(1, figsize=(9, 6))

ax = fig.add_subplot(111)

bp = ax.boxplot(boxplot_data)

plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='darkgray')
plt.setp(bp['fliers'], color='red', marker='+')

ax.set_xticklabels(["2 / 16", "2 / 128", "2 / 256",
                    "4 / 32", "4 / 256", "4 / 512",
                    "VM Seq", "Seq"])

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)

ax.set_title("TSP Solution (85900 Cities) Cost After Tuning for 15 minutes (4 runs)")
ax.set_xlabel("VM Configuration")
ax.set_ylabel("Solution Cost")

fig.savefig('pla85900_15min_comparison.eps', format = 'eps', dpi = 1000)
