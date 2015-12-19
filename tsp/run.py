#! /usr/bin/env python2.7

from subprocess import call

runs              = [# (machines, results/machine, runtime)
                     # 4 Hours
                     ( 2, 128, 900),
                     ( 2, 256, 900),
#                     ( 2,  16, 900),
#                     ( 2,  32, 900),
                     # 4 Hours
                     ( 4, 256, 900),
                     ( 4, 512, 900),
#                     ( 4,  32, 900),
#                     ( 4,  64, 900),
                     # 4 Hours
#                     ( 8,   8, 900),
#                     ( 8,  32, 900),
#                     ( 8,  64, 900),
#                     ( 8, 128, 900),
                     # 4 Hours
#                     (16,  16, 900),
#                     (16,  64, 900),
#                     (16, 128, 900),
#                     (16, 256, 900)
                     ]

executions        = 4

instance_number   = runs[0][0]
parallelism_value = runs[0][1]
run_time          = runs[0][2]

repo              = "--repo=https://github.com/phrb/gce_autotuning_experiments.git"
project           = "--project=autotuning-1116"
interface_path    = "--interface-path=tsp/tuner.py"
interface_name    = "--interface-name=TSP"

for i in range(len(runs)):
    print "[Initializing Tuning Run {0}]".format(i + 1)

    cmd = "/usr/bin/env python2.7 tuner.py "

    instance_number   = runs[i][0]
    parallelism_value = runs[i][1]
    run_time          = runs[i][2]

    instances         = "--instances={0}".format(instance_number)
    parallelism       = "--parallelism={0}".format(parallelism_value)
    stop_after        = "--stop-after={0}".format(run_time)

    for j in range(executions):
        # (run_id, instances, parallelism, runtime, run_number)
        log_dir = "results/pla85900/run_{0}_inst_{1}_para_{2}_time_{3}_{4}".format(i + 1,
                                                                                   instance_number,
                                                                                   parallelism_value,
                                                                                   run_time,
                                                                                   j + 1)

        results_log = "--results-log={0}/results.log".format(log_dir)
        last_log    = "--log-last={0}/last.txt".format(log_dir)

        call("mkdir {0}".format(log_dir), shell = True)

        print "[Starting Run {0}]".format(i + 1)
        cmd += "{0} {1} {2} {3} {4} {5} {6} {7} {8}".format(stop_after,
                                                            repo,
                                                            project,
                                                            interface_path,
                                                            interface_name,
                                                            instances,
                                                            parallelism,
                                                            results_log,
                                                            last_log)

        retcode = call(cmd, shell = True)

        call("rm -rf opentuner.log opentuner.db", shell = True)

        print "[Run {0} is done]".format(i + 1)
