
__module_name__ = "__init__.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import API ------------------------------------------------------------------
from . import _construction as build
from . import _style as style
from . import _utilities as ut

# import main API functions ---------------------------------------------------
from ._plot._Plot import _Plot as Plot
from ._plot._quick_plot import _quick_plot as quick_plot
from ._construction._save_figure import _save_figure as save

# fetch color palettes --------------------------------------------------------
import os as _os
from ._utilities import _fetch_color_palettes
from ._color_palettes._ColorPalettes import _ColorPalettes

dest = _os.path.join(__file__, "_color_palettes/_palette_pkl_src/")
url = "https://github.com/mvinyard/vinplots/raw/main/vinplots/_color_palettes/_palette_pkl_src/"
_fetch_color_palettes(url, dest_dir=dest)

colors = _ColorPalettes()
