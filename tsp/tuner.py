import argparse
import logging
import subprocess
import os

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
                        default  = 532,
                        help     = "Instance size.")


class TSP(MeasurementInterface):
    def run(self, desired_result, input, limit):
        cfg  = desired_result.configuration.data
        tour = cfg[0]
        cmd  = "./tour_cost "
        for city in tour:
            cmd += str(city + 1) + " "

        logger = logging.getLogger("MeasurementServer")
        logger.debug("Executing: {0}".format(cmd))
        logger.debug("Directory: {0}".format(os.getcwd()))

        result = subprocess.check_output(cmd, shell = True)
        cost   = float(result)
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
