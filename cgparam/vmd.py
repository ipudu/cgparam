###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

from .base import Loader

class VMD(Loader):
    """control VMD"""
    def __init__(self, filename):
        super(VMD, self).__init__(filename)
        atoms = self.constants['atoms'].replace(' ', '').split(',')
        self.atoms = atoms

    def gofr_tcl(self, center, around, s=5000, e=-1, freq=1):
        """make gofr TCL input for VMD"""
        i = self.atoms.index(center) + 1
        j = self.atoms.index(around) + 1

        filename = 'gofr_{}-{}.tcl'.format(center, around)
        
        with open(filename, 'w') as f:
            f.write('set sel1 [atomselect top "type {:d}"]\n'.format(i))
            f.write('set sel2 [atomselect top "type {:d}"]\n'.format(j))
            f.write('set gr [measure gofr ')
            f.write('$sel1 $sel2 delta .1 rmax 10 usepbc 1 selupdate 1 ')
            f.write('first {:d} last {:d} step {:d}]\n'.format(s, e, freq))
            f.write('set outfile [open gofr_{}-{}.dat w]\n'.format(center, around))
            f.write('set r [lindex $gr 0]\n')
            f.write('set gr2 [lindex $gr 1]\n')
            f.write('set igr [lindex $gr 2]\n')
            f.write('foreach j $r k $gr2 l $igr {\n')
            f.write('    puts $outfile "$j $k $l"\n')
            f.write('}\n')
            f.write('close $outfile\n')
    
    def load_tcl(self, data, trajectory, pairs, load_t=10000, interval_t=1000):
        """create TCL input of reading data and traj for VMD"""
        with open('load.tcl', 'w') as f:
            f.write('topo readlammpsdata {}\n'.format(data))
            f.write('mol addfile {}\n'.format(trajectory))
            for a, b in pairs:
                f.write('after {:d} source gofr_{}-{}.tcl\n'.format(load_t, a, b))
                load_t += interval_t
