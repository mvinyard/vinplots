
__module_name__ = "__init__.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import API ------------------------------------------------------------------
from . import _utils as ut

# import main API functions ---------------------------------------------------

# fetch color palettes --------------------------------------------------------
from ._color_palettes._ColorPalettes import _ColorPalettes
colors = _ColorPalettes()


from . import _core