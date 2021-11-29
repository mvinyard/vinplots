

import numpy as np
import matplotlib.pyplot as plt

from .._construction._funcs._construct_plot_layout import _construct_plot_layout
from .._style._funcs._modify_axis_spines import _modify_axis_spines, _modify_all_ax_spines


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
        
    def modify_spines(self,
                      ax,
                      color=False,
                      spines_to_color=False,
                      spines_to_delete=False,
                      spines_to_move=False,
                      spines_positioning="outward",
                      spines_positioning_amount=0,):
        
        """
        
        """
        
            
        if ax=="all":
            mod_func = _modify_all_ax_spines
            ax=self.AxesDict
        else:
            mod_func = _modify_axis_spines
            
        mod_func(ax, 
                 color, 
                 spines_to_color, 
                 spines_to_delete,
                 spines_to_move,
                 spines_positioning,
                 spines_positioning_amount,)
        