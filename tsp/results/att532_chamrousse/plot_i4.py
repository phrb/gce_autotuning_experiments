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

i4_p64_path       = "inst_4_para_64/run_2_inst_4_para_64_time_900_1/"
i4_p64_data       = []
i4_p64_sample_run = [[], []]

i4_p4_path        = "inst_4_para_4/run_3_inst_4_para_4_time_900_1/"
i4_p4_data        = []
i4_p4_sample_run  = [[], []]

i4_p32_path        = "inst_4_para_32/run_1_inst_4_para_32_time_900_1/"
i4_p32_data        = []
i4_p32_sample_run  = [[], []]

i4_p16_path       = "inst_4_para_16/run_1_inst_4_para_16_time_900_1/"
i4_p16_data       = []
i4_p16_sample_run = [[], []]

# OpenTuner Sequential
ot_path       = "./"
ot_data       = []
ot_sample_run = [[], []]

with open(i4_p64_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i4_p64_sample_run[0].append(float(point[0]))
        i4_p64_sample_run[1].append(float(point[1]))

with open(i4_p4_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i4_p4_sample_run[0].append(float(point[0]))
        i4_p4_sample_run[1].append(float(point[1]))

with open(i4_p32_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i4_p32_sample_run[0].append(float(point[0]))
        i4_p32_sample_run[1].append(float(point[1]))

with open(i4_p16_path + "results.log") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        i4_p16_sample_run[0].append(float(point[0]))
        i4_p16_sample_run[1].append(float(point[1]))

with open(ot_path + "sequential.txt") as file:
    text_points = file.read().splitlines()
    for line in text_points:
        point = line.split(" ")
        ot_sample_run[0].append(float(point[0]))
        ot_sample_run[1].append(float(point[1]))

fig = plt.figure(1, figsize=(7, 6))
ax = fig.add_subplot(111)

ax.set_xlim([-4, max(max(i4_p64_sample_run[0]), max(i4_p4_sample_run[0]),
                     max(i4_p32_sample_run[0]), max(i4_p16_sample_run[0]),
                     max(ot_sample_run[0])) + 4])

ax.set_ylim([min(min(i4_p64_sample_run[1]), min(i4_p4_sample_run[1]),
                 min(i4_p32_sample_run[1]), min(i4_p16_sample_run[1]),
                 min(ot_sample_run[1])) - 50000,
             max(max(i4_p64_sample_run[1]), max(i4_p4_sample_run[1]),
                 max(i4_p64_sample_run[1]), max(i4_p4_sample_run[1]),
                 max(ot_sample_run[1])) + 50000])

i4_p64_b = ax.scatter(i4_p64_sample_run[0], i4_p64_sample_run[1], marker = 'x', color = 'c')
ax.plot(i4_p64_sample_run[0], i4_p64_sample_run[1], color = 'c')

i4_p4_b = ax.scatter(i4_p4_sample_run[0], i4_p4_sample_run[1], marker = 'o', color = 'g')
ax.plot(i4_p4_sample_run[0], i4_p4_sample_run[1], color = 'g')

i4_p32_b = ax.scatter(i4_p32_sample_run[0], i4_p32_sample_run[1], marker = 'x', color = 'r')
ax.plot(i4_p32_sample_run[0], i4_p32_sample_run[1], color = 'r')

i4_p16_b = ax.scatter(i4_p16_sample_run[0], i4_p16_sample_run[1], marker = 'o', color = 'b')
ax.plot(i4_p16_sample_run[0], i4_p16_sample_run[1], color = 'b')

ot_b = ax.scatter(ot_sample_run[0], ot_sample_run[1], marker = 'o', color = 'black')
ax.plot(ot_sample_run[0], ot_sample_run[1], color = 'black')

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)

ax.set_xlabel("Tuning Time")
ax.set_ylabel("Solution Cost")

plt.legend((i4_p4_b, i4_p16_b, i4_p32_b, i4_p64_b, ot_b),
           ('4 Instances, 4 Requests', '4 Instances, 16 Requests',
            '4 Instances, 32 Requests', '4 Instances, 64 Requests',
            'Sequential'), prop = {'size': 14})

fig.savefig('i4_p_n_comparison.eps', format = 'eps', dpi = 1000)
