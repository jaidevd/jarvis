#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the BSD 3-clause license.

"""

"""


from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from chaco.api import Plot, ArrayPlotData
from chaco.tools.api import ScatterInspector
from enable.component_editor import ComponentEditor


class Demo(HasTraits):

    plot = Instance(Plot)

    view = View(Item('plot', editor=ComponentEditor(), show_label=False))

    def _plot_default(self):
        import numpy as np
        data = np.random.normal(size=(10, 2))
        apl = ArrayPlotData(x=data[:, 0], y=data[:, 1])
        plot = Plot(apl)
        scatter = plot.plot(('x', 'y'), type='scatter')[0]
        self.inspector = ScatterInspector(scatter)
        scatter.tools.append(self.inspector)
        return plot

if __name__ == '__main__':
    demo = Demo()
    demo.configure_traits()
    print demo.inspector.component.index.metadata
