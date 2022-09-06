
__module_name__ = "__init__.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# -----------------------------------------------------------------------------
from . import _construction as build
from . import _style as style
from . import _utilities as ut


# -----------------------------------------------------------------------------
from ._plot._Plot import _Plot as Plot
from ._plot._quick_plot import _quick_plot as quick_plot
from ._construction._save_figure import _save_figure as save

# -----------------------------------------------------------------------------
from ._color_palettes._ColorPalettes import _ColorPalettes
colors = _ColorPalettes()
