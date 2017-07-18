###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

import shutil
import os
import datetime

def cp_dir(o_dir, t_dir):
    t_dir =  t_dir + '_' + datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    shutil.copytree(o_dir, t_dir)

if __name__ == '__main__':
    cp_dir('foo', 'bar')