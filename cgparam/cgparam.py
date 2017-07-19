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

from . import sw, plot

def get_parser():
    parser = argparse.ArgumentParser(description='cgparam: Parameterization of a \
                                                  coarse-grained model with \
                                                  Stillinger-Weber potentials')
    parser.add_argument('input', type=str, nargs='?',help='input file for cgparam')
    parser.add_argument('-t','--task', default='sw', type=str,
                        help=' type of task: sw,swm,plot (default: sw)')
    parser.add_argument('-p','--parameter', type=str,
                    help=' parameter files(CSV format): twobody, threebody')
    parser.add_argument('-m','--modification', type=str,
                    help=' arguments to modify SW CSV file (order: paramname,number,i,j,k)')
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

        #SW
        if args['task'] == 'sw':
            tasker = sw.SW(args['input'])
            if not args['parameter']:
                raise StandardError("Twobody and threebody SW parammeters are not provided!")
            else:
                two, three = args['parameter'].split(',')
                header_b2, b2 = tasker.csv_reader(two)
                header_b3, b3 = tasker.csv_reader(three)
                tasker.lammps_input_writer(args['sw'], b2, b3)

        #SWM
        if args['task'] == 'swm':
            tasker = sw.SW(args['input'])
            if not args['parameter']:
                raise StandardError("Twobody and threebody SW parammeters are not provided!")
            else:
                two, three = args['parameter'].split(',')
                header_b2, b2 = tasker.csv_reader(two)
                header_b3, b3 = tasker.csv_reader(three)
                if not args['modification']:
                    raise StandardError("paramname, number, i, j, k \
                                         are not provided!\n")
                else:
                    m = args['modification'].replace(' ', '').split(',')
                    if len(m) == 4:
                        paramname, number, i, j = m
                        b2, b3 = tasker.modify_data(b2, b3, 
                                                    paramname, number, 
                                                    i, j)
                    else:
                        paramname, number, i, j, k = m
                        b2, b3 = tasker.modify_data(b2, b3, 
                                                    paramname, number, 
                                                    i, j, k)

                #generated new twobody and threebody parameters
                tasker.csv_writer(b2, two)
                tasker.csv_writer(b3, three)

                #generated SW input for LAMMPS
                tasker.lammps_input_writer(args['sw'], b2, b3)
        
        #plot
        if args['task'] == 'plot':
            tasker = plot.Plot(args['input'])
            for filename in tasker.gofr:
                tasker.plot_gofr(filename)

if __name__ == '__main__':
    command_line_runner()