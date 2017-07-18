###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

class SSH(object):
    """SSH"""
    def __init__(self, username, hostname):
        self.username = username
        self.hostname = hostname

    def make_bash(self, filename):
        """make a bash file"""
        with open(filename, 'w') as f:
            f.write('#!/bin/bash\n\n')
            f.write("ssh -t -t {}@{}<<'ENDSSH'\n".format(self.username, 
                                                         self.hostname))
            f.write('exit\n')
            f.write('ENDSSH\n')

    def upload(self):
        pass

if __name__ == '__main__':
    connector = SSH('pdu','qb.loni.org')
    connector.make_bash('test.sh')
