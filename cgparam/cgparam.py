###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

from __future__ import print_function
import argparse

from . import sw

def get_parser():
    parser = argparse.ArgumentParser(description='cgparam: Parameterization of a \
                                                  coarse-grained model with \
                                                  Stillinger-Weber potentials')
    parser.add_argument('input', type=str, nargs='?',help='input file for cgparam')
    parser.add_argument('-t','--task', default='sw', type=str,
                        help=' type of task: sw,plot (default: sw)')
    parser.add_argument('-p','--parameter', default='2b.csv,3b.csv', type=str,
                    help=' parameter files(CSV format): twobody, threebody (default: 2b.csv,3b.csv)')
    parser.add_argument('-s','--sw', default=None, type=str,
                    help=' output name of Stillinger-Web input for LAMMPS (default: None)')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['input']:
        parser.print_help()
        return

    if args['task']:
        if args['task'] == 'sw':
            tasker = sw.SW(args['input'])
            if args['parameter']:
                two, three = args['parameter'].split(',')
                header_b2, b2 = tasker.csv_reader(two)
                header_b3, b3 = tasker.csv_reader(three)
                tasker.lammps_input_writer(args['sw'], b2, b3)

if __name__ == '__main__':
    command_line_runner()