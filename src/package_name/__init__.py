from importlib.metadata import version, PackageNotFoundError

__version__ = "0.0.0"

try:
    __version__ = version("calicolabs-$HYPHENATED_PACKAGE_NAME")
except PackageNotFoundError:
    pass
