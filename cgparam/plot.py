###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, save, output_file
from bokeh.models import HoverTool

class plot(object):
    """plotting class"""

    def __init__(self):
        pass
    
    def plot_gr_r(self, filename, outname):
        """plot radial distribution function and coordination number"""
        data = np.loadtxt(filename)

        #r, gr, c
        r = data[:,0]
        gr = data[:,1]
        c = data[:,2]
        
        #show the data points
        hover = HoverTool(tooltips=[
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),])

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select, hover"

        #g(r)
        p1 = figure(title="Radial Distribution Function", tools=TOOLS)
        
        p1.circle(r, gr, legend="g(r)")
        p1.line(r, gr, legend="g(r)")

        #Int(r)
        p2 = figure(title="Coordination Number", tools=TOOLS)
        
        p2.circle(r, c, legend="Int(r)")
        p2.line(r, c, legend="Int(r)")
        
        output_file(outname+".html")
        save(gridplot(p1, p2, ncols=2, plot_width=400, plot_height=400))

if __name__ == '__main__':
    a = plot()
    a.plot_gr_r('gofr_AA_O-O.dat','gofr_AA_O-O')