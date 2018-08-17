"""Init file for Geizhals."""
from pkg_resources import get_distribution, DistributionNotFound
from .geizhals import Device, Geizhals

NAME = "geizhals"
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
