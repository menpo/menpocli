
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


# Global URL for the current Menpo server for storing files
MENPO_SERVER_URL = 'https://s3-eu-west-1.amazonaws.com/cdn.menpo.org/'
