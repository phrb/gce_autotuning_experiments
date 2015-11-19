import adddeps

import argparse
import logging
import subprocess
import os
from uuid import uuid4

import opentuner
from opentuner.search.manipulator import ConfigurationManipulator, PermutationParameter
from opentuner.measurement import MeasurementInterface

import measurement_client
from measurement_client.client import MeasurementClient
from measurement_client.gce_interface.interface import GCEInterface

log = logging.getLogger(__name__)

parsers = opentuner.argparsers() + measurement_client.argparsers()

argparser = argparse.ArgumentParser(parents = parsers)
argparser.add_argument( "-last", "--log-last",
                        dest     = "loglast",
                        type     = str,
                        required = True,
                        help     = "File to save best configuration to.")
argparser.add_argument( "-size", "--instance-size",
                        dest     = "size",
                        type     = int,
                        default  = 85900,
                        help     = "Instance size.")


class TSP(MeasurementInterface):
    def run(self, desired_result, input, limit):
        filename = "{0}".format(uuid4())

        cfg  = desired_result.configuration.data
        tour = cfg[0]
        round_trip = ""
        cmd  = "./tour_cost {0}".format(filename)

        for city in tour:
            round_trip += "{0}\n".format(city + 1)

        round_trip += "{0}\n".format(tour[0] + 1)

        with open(filename, "w") as file:
            file.write(round_trip)

        logger = logging.getLogger("MeasurementServer")
        logger.debug("Executing: {0}".format(cmd))
        logger.debug("Directory: {0}".format(os.getcwd()))

        result = subprocess.check_output(cmd, shell = True)
        cost   = float(result)

        subprocess.check_output("rm {0}".format(filename), shell = True)

        return opentuner.resultsdb.models.Result(time = cost)

    def manipulator(self):
        manipulator = ConfigurationManipulator()
        manipulator.add_parameter(PermutationParameter(0, range(SIZE)))
        return manipulator

    def save_final_config(self, configuration):
        print "[Saving Best Configuration]"
        self.driver.gce_interface.delete_all()

        cfg = configuration.data
        tour = cfg[0]
        cmd  = ""

        for city in tour:
            cmd += str(city + 1) + "\n"

        cmd += str(tour[0] + 1) + "\n"

        with open(LOG_FILE, "a+") as file:
            file.write(cmd)

        print "[Done]"

    @classmethod
    def main(cls, args, *pargs, **kwargs):
        from opentuner.tuningrunmain import TuningRunMain
        return TuningRunMain(cls(args, *pargs, **kwargs), args,
                             measurement_driver = MeasurementClient).main()

if __name__ == '__main__':
    args = argparser.parse_args()
    LOG_FILE = args.loglast
    SIZE     = args.size
    TSP.main(args)
