#! /usr/bin/python

import os
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt


plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')

font = {'family' : 'serif',
        'size'   : 16}

mpl.rc('font', **font)

i2_p16_path       = "inst_2_para_16/run_2_inst_2_para_16_time_900_3/"
i2_p16_data       = []
i2_p16_sample_run = [[], []]

i2_p2_path        = "inst_2_para_2/run_1_inst_2_para_2_time_900_1/"
i2_p2_data        = []
i2_p2_sample_run  = [[], []]

i2_p8_path        = "inst_2_para_8/run_1_inst_2_para_8_time_900_1/"
i2_p8_data        = []
i2_p8_sample_run  = [[], []]

i2_p32_path       = "inst_2_para_32/run_2_inst_2_para_32_time_900_1/"
i2_p32_data       = []
i2_p32_sample_run = [[], []]

# OpenTuner Sequential
ot_path       = "./"
ot_data       = []
ot_sample_run = [[], []]

with open(i2_p16_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i2_p16_sample_run[0].append(float(point[0]))
        i2_p16_sample_run[1].append(float(point[1]))

with open(i2_p2_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i2_p2_sample_run[0].append(float(point[0]))
        i2_p2_sample_run[1].append(float(point[1]))

with open(i2_p8_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i2_p8_sample_run[0].append(float(point[0]))
        i2_p8_sample_run[1].append(float(point[1]))

with open(i2_p32_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i2_p32_sample_run[0].append(float(point[0]))
        i2_p32_sample_run[1].append(float(point[1]))

with open(ot_path + "sequential.txt") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        ot_sample_run[0].append(float(point[0]))
        ot_sample_run[1].append(float(point[1]))

fig = plt.figure(1, figsize=(7, 6))
ax = fig.add_subplot(111)

ax.set_xlim([-4, max(max(i2_p16_sample_run[0]), max(i2_p2_sample_run[0]),
                     max(i2_p8_sample_run[0]), max(i2_p32_sample_run[0]),
                     max(ot_sample_run[0])) + 4])

ax.set_ylim([min(min(i2_p16_sample_run[1]), min(i2_p2_sample_run[1]),
                 min(i2_p8_sample_run[1]), min(i2_p32_sample_run[1]),
                 min(ot_sample_run[1])) - 50000,
             max(max(i2_p16_sample_run[1]), max(i2_p2_sample_run[1]),
                 max(i2_p8_sample_run[1]), max(i2_p32_sample_run[1]),
                 max(ot_sample_run[1])) + 50000])

i2_p16_b = ax.scatter(i2_p16_sample_run[0], i2_p16_sample_run[1], marker = 'x', color = 'c')
ax.plot(i2_p16_sample_run[0], i2_p16_sample_run[1], color = 'c')

i2_p2_b = ax.scatter(i2_p2_sample_run[0], i2_p2_sample_run[1], marker = 'o', color = 'g')
ax.plot(i2_p2_sample_run[0], i2_p2_sample_run[1], color = 'g')

i2_p8_b = ax.scatter(i2_p8_sample_run[0], i2_p8_sample_run[1], marker = 'x', color = 'r')
ax.plot(i2_p8_sample_run[0], i2_p8_sample_run[1], color = 'r')

i2_p32_b = ax.scatter(i2_p32_sample_run[0], i2_p32_sample_run[1], marker = 'o', color = 'b')
ax.plot(i2_p32_sample_run[0], i2_p32_sample_run[1], color = 'b')

ot_b = ax.scatter(ot_sample_run[0], ot_sample_run[1], marker = 'o', color = 'black')
ax.plot(ot_sample_run[0], ot_sample_run[1], color = 'black')

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)

ax.set_xlabel("Tuning Time")
ax.set_ylabel("Solution Cost")

plt.legend((i2_p2_b, i2_p8_b, i2_p16_b, i2_p32_b, ot_b),
           ('2 Instances, 2 Requests', '2 Instances, 8 Requests',
            '2 Instances, 16 Requests', '2 Instances, 32 Requests',
            'Sequential'), prop = {'size' : 14})

fig.savefig('i2_p_n_comparison.eps', format = 'eps', dpi = 1000)
