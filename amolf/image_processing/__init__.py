import os
import glob

SOURCE_FILES = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(f)[: -3] for f in SOURCE_FILES]

__doc__ = """\
Module for advanced image processing, segmentation, fourier spatial analysis etc.
"""

from .popups import *