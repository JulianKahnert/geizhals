"""Init file for Geizhals."""
from .geizhals import (Geizhals, Device)
from pkg_resources import get_distribution, DistributionNotFound

NAME = "geizhals"
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
