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

d1_path  = "inst_2_para_2/"
d1_data  = []

d2_path  = "inst_2_para_8/"
d2_data  = []

d3_path  = "inst_2_para_16/"
d3_data  = []

d4_path  = "inst_2_para_32/"
d4_data  = []

d5_path  = "inst_4_para_4/"
d5_data  = []

d6_path  = "inst_4_para_16/"
d6_data  = []

d7_path  = "inst_4_para_32/"
d7_data  = []

d8_path  = "inst_4_para_64/"
d8_data  = []

d9_path  = "sequential/"
d9_data  = []

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
    with open(d7_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d7_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d8_path):
    with open(d8_path + run + "/results.log") as file:
        best = file.read().splitlines()
        d8_data.append(float(best[-1].split(" ")[1]))

for run in os.listdir(d9_path):
    with open(d9_path + run + "/best.txt") as file:
        best = file.read().splitlines()
        d9_data.append(float(best[-1].split(" ")[1]))

boxplot_data = [d1_data, d2_data, d3_data,
                d4_data, d5_data, d6_data,
                d7_data, d8_data, d9_data]

fig = plt.figure(1, figsize=(7, 6))

ax = fig.add_subplot(111)

bp = ax.boxplot(boxplot_data)

plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='darkgray')
plt.setp(bp['fliers'], color='red', marker='+')

ax.set_xticklabels(["2 / 2", "2 / 8", "2 / 16", "2 / 32",
                    "4 / 4", "4 / 16", "4 / 32", "4 / 64",
                    "Sequential"], rotation = 45)

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)

ax.set_title("TSP Solution (85900 Cities) Cost After Tuning for 15 minutes (4 runs)")
ax.set_ylabel("Solution Cost")

fig.tight_layout()

fig.savefig('att532_15min_boxplot.eps', format = 'eps', dpi = 1000)
