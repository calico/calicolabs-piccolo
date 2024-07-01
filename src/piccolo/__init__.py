from importlib.metadata import version, PackageNotFoundError

__version__ = "0.0.0"

try:
    __version__ = version("calicolabs-piccolo")
except PackageNotFoundError:
    pass
