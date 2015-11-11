#! /usr/bin/env python2.7

from subprocess import call

runs = [( 1, 64, 600),
        ( 2, 64, 600)]
        ( 4, 64, 600)]
        ( 8, 64, 600)]
        (16, 64, 600)]

instance_number   = runs[0][0]
parallelism_value = runs[0][1]
run_time          = runs[0][2]

repo              = "--repo=https://github.com/phrb/gce_autotuning_example.git"
project           = "--project=autotuning-1116"
interface_path    = "--interface-path=tuner.py"
interface_name    = "--interface-name=TSP"
results_log       = "--results-log=results.log"


call("mkdir results", shell = True)

for i in range(len(runs)):
    print "[Initializing Tuning Run {0}]".format(i + 1)

    cmd = "/usr/bin/env python2.7 tuner.py "

    instance_number   = runs[0][0]
    parallelism_value = runs[0][1]
    run_time          = runs[0][2]

    instances         = "--instances={0}".format(instance_number)
    parallelism       = "--parallelism={0}".format(parallelism_value)
    stop_after        = "--stop-after={0}".format(run_time)

    log_dir = "results/run_{0}_inst_{1}_para_{2}_time_{3}".format(i + 1,
                                                                  instance_number,
                                                                  parallelism_value,
                                                                  run_time)

    call("mkdir {0}".format(log_dir), shell = True)

    print "[Starting Run {0}]".format(i + 1)
    cmd += "{0} {1} {2} {3} {4} {5} {6} {7}".format(stop_after,
                                                    repo,
                                                    project,
                                                    interface_path,
                                                    interface_name,
                                                    instances,
                                                    parallelism,
                                                    results_log)
    print "[Run {0} is done]".format(i + 1)

    retcode = call(cmd, shell = True)
