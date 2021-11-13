

import numpy as np
import matplotlib.pyplot as plt

from ._construct_plot_layout import _construct_plot_layout


class _Plot:
    def __init__(self, tight=True, grid=True):

        """Instantiates a general plot space"""

    def construct(
        self,
        nplots,
        ncols=4,
        figsize_width=1,
        figsize_height=1,
        figsize=False,
        hspace=0.18,
        width_ratios=False,
    ):

        """
        Setup figure layout.
        nplots
        ncols
        figsize_width
        figsize_height
        """
        
        assert nplots >= ncols, print("nplots must be >= ncols")
        
        self.nplots = nplots
        self.hspace = hspace
        self.ncols = ncols
        
        if figsize:
            self.figsize_width = self.figsize_height = figsize
        else:
            self.figsize_width = figsize_width
            self.figsize_height = figsize_height
        
        if width_ratios:
            self.width_ratios = width_ratios
        else:
            self.width_ratios = np.ones(min(self.nplots, self.ncols))

        self.fig, self.AxesDict = _construct_plot_layout(
            nplots=self.nplots,
            ncols=self.ncols,
            figsize_width=self.figsize_width,
            figsize_height=self.figsize_height,
            grid_hspace=self.hspace,
            width_ratios=self.width_ratios,
        )