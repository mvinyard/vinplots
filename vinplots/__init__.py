# __init__.py

__module_name__ = "__init__.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])

# package imports #
# --------------- #
import matplotlib as _mpl
import matplotlib.font_manager as _font_manager
import os as _os
import subprocess as _subprocess

def _download_mscore_fonts():
    
    """"""
    
    check_package = _subprocess.run(['conda', 'search', 'mscore'], stdout=subprocess.PIPE, stderr=False).stdout.decode().split('\n')
    if len(check_package) > 3:
        return "installed"
    else:
        download_log = _subprocess.run(['conda', 'install', '-c', 'conda-forge', 'mscorefonts', '-y'], stdout=subprocess.PIPE, stderr=False)
        return download_log

# matplotlib rcParams #
# ------------------- #

# install mscorefonts and clear the previous parameter cache file.
_os.system("conda install -c conda-forge mscorefonts -y")
_mscore_install = _download_mscore_fonts()

_font = {"size": 12}
_mpl.rc(_font)
_mpl.rcParams["font.sans-serif"] = "Arial"
_mpl.rcParams["font.family"] = "sans-serif"


# import sub-packages and Plot module #
# ----------------------------------- #
from ._plot._PlotModule import _Plot as Plot
from . import _color_palettes as colors
