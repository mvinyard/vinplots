
# -- import packages: ----------------------------------------------------------
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import math


# -- define types: -------------------------------------------------------------
from typing import List
NoneType = type(None)


# -- import local dependencies: ------------------------------------------------
from ._auto_parse_base_class import AutoParseBase
from ._plot_dimensions import PlotDimensions
from ._style_spines import style_spines

# -- Main class: ---------------------------------------------------------------
class Plot(AutoParseBase):
    def __init__(
        self,
        nplots: int =1,
        ncols: int =1,
        scale: float =None,
        width: float =1,
        height: float =1,
        hspace: float =0,
        wspace: float =0,
        width_ratios: List[float]=None,
        height_ratios: List[float]=None,
    ):

        if not isinstance(scale, NoneType):
            height = width = scale
            
        if (nplots > ncols) and (nplots < 4):
            ncols = nplots
        else:
            ncols = 4
            

        self.__parse__(locals(), private=["width", "height"])

        self.plot_dims = PlotDimensions(
            self.ncols, self.nrows, self._width, self._height
        )
        self.height = self.plot_dims.height
        self.width = self.plot_dims.width

    def linearize_axes(self):

        axes = []

        for i, row in self.AxesDict.items():
            for j, col in row.items():
                axes.append(self.AxesDict[i][j])
        return axes

    @property
    def figure(self):
        return plt.figure(figsize=(self.width, self.height))

    @property
    def nrows(self):
        return math.ceil(self.nplots / self.ncols)

    @property
    def gridspec(self):
        return GridSpec(
            nrows=self.nrows,
            ncols=self.ncols,
            width_ratios=self.width_ratios,
            height_ratios=self.height_ratios,
            hspace=self.hspace,
            wspace=self.wspace,
        )

    def __call__(self, linearize=True):

        plot_count = 0
        self.AxesDict = {}

        self.fig = self.figure
        gridspec = self.gridspec

        for ax_i in range(self.nrows):
            self.AxesDict[ax_i] = {}
            for ax_j in range(self.ncols):
                plot_count += 1
                self.AxesDict[ax_i][ax_j] = self.fig.add_subplot(gridspec[ax_i, ax_j])
                if plot_count >= self.nplots:
                    break

        if linearize:
            return self.fig, self.linearize_axes()
        return self.fig, self.AxesDict


# -- API-facing function: ------------------------------------------------------
def plot(
    nplots: int = 1,
    ncols: int = 1,
    scale: float = None,
    width: float = 1,
    height: float = 1,
    hspace: float = 0,
    wspace: float = 0,
    width_ratios: List[float] = None,
    height_ratios: List[float] = None,
    linearize=True,
    color=[None],
    move=[0],
    delete_spines=[[]],
    color_spines=[[]],
    move_spines=[[]],
):
    """
    Parameters:
    -----------

    Returns:
    --------
    fig, axes
    """

    plot_obj = Plot(
        nplots=nplots,
        ncols=ncols,
        scale=scale,
        width=width,
        height=height,
        hspace=hspace,
        wspace=wspace,
        width_ratios=width_ratios,
        height_ratios=height_ratios,
    )
    
    fig, axes = plot_obj(linearize=linearize)
        
    # styling in function requires linearization
    if linearize:
        for n, ax in enumerate(axes):
            style_spines(
                ax,
                color=color[n],
                move=move[n],
                delete_spines=delete_spines[n],
                color_spines=color_spines[n],
                move_spines=move_spines[n],
            )
        
    return fig, axes
