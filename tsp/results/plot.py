#! /usr/bin/python

import os
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt


plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')

i2_p16_path       = "run_2_inst_2_para_16_time_900_3/"
i2_p16_data       = []
i2_p16_sample_run = [[], []]

i4_p32_path       = "run_1_inst_4_para_32_time_900_1"
i4_p32_data       = []
i4_p32_sample_run = [[], []]

with open(i2_p16_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i2_p16_sample_run[0].append(float(point[0]))
        i2_p16_sample_run[1].append(float(point[1]))

with open(i4_p32_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i4_p32_sample_run[0].append(float(point[0]))
        i4_p32_sample_run[1].append(float(point[1]))

fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)

ax.set_xlim([-4, max(max(i2_p16_sample_run[0]), max(i4_p32_sample_run[0])) + 4])

ax.set_ylim([min(min(i2_p16_sample_run[1]), min(i4_p32_sample_run[1])) - 50000, max(max(i2_p16_sample_run[1]), max(i4_p32_sample_run[1])) + 50000])

i2_p16_b = ax.scatter(i2_p16_sample_run[0], i2_p16_sample_run[1], marker = 'x', color = 'c')
ax.plot(i2_p16_sample_run[0], i2_p16_sample_run[1], color = 'c')

i4_p32_b = ax.scatter(i4_p32_sample_run[0], i4_p32_sample_run[1], marker = 'o', color = 'g')
ax.plot(i4_p32_sample_run[0], i4_p32_sample_run[1], color = 'g')

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)

ax.set_title("Best TSP Solution (532 Cities) during a Tuning Run")
ax.set_xlabel("Tuning Time")
ax.set_ylabel("Solution Cost")

plt.legend((i2_p16_b, i4_p32_b),
           ('StochasticSearch.jl', 'OpenTuner'))

fig.savefig('att532_10min_best_comparison.eps', format = 'eps', dpi = 1000)
