###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

import os
import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, save, output_file
from bokeh.models import HoverTool

from .base import Loader

class Plot(Loader):
    """plotting class"""
    def __init__(self, filename):
        super(Plot, self).__init__(filename)
        self.gofr = self.constants['gofr']

    def plot_gofr(self, filename):
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
        
        #get the prefix of filename
        base = os.path.basename(filename)
        filename = os.path.splitext(base)[0]
        output_file(filename + ".html")
        save(gridplot(p1, p2, ncols=2, plot_width=400, plot_height=400))