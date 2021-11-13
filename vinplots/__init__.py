# __init__.py


__module_name__ = "__init__.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# package imports #
# --------------- #
import matplotlib
import matplotlib.font_manager
import os


# matplotlib rcParams #
# ------------------- #


# clear the previous parameter cache file.
os.system("rm ~/.cache/matplotlib -rf")

font = {"size": 12}
matplotlib.rc(font)
matplotlib.rcParams["font.sans-serif"] = "Arial"
matplotlib.rcParams["font.family"] = "sans-serif"


# import sub-packages #
# ------------------- #
from . import _construction as build