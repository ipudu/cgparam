###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

from yaml import load, dump

class Loader(object):
    """base class for loading input file"""

    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.constants = load(f)