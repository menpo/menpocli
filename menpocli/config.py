import os
from pathlib import Path
from .utils import create_path, load_yaml, save_yaml, norm_path
from .exception import MissingConfigKeyError


DEFAULT_CACHE_DIR = norm_path('~/menpocache')


@create_path
def user_menpo_config_dir():
    return Path(os.path.expanduser('~')) / '.menpo'


def user_settings_path():
    return user_menpo_config_dir() / 'settings.yaml'


def save_user_settings(c):
    if user_settings_path().exists():
        # Update existing config file with new information
        config = load_yaml(user_settings_path())
        config.update(c)
    else:
        config = c
    save_yaml(config, user_settings_path())


def user_settings():
    try:
        return load_yaml(user_settings_path())
    except IOError:
        # Create an empty default config file.
        save_user_settings({})
        return user_settings()


def clear_user_settings():
    p = user_settings_path()
    if p.is_file():
        p.unlink()


@create_path
def resolve_cache_dir(verbose=False):
    try:
        cache_dir = Path(user_settings()['cache_dir'])
    except KeyError as e:
        raise MissingConfigKeyError(e.args[0])
    if verbose:
        print('Cache dir: {}'.format(cache_dir))
    return cache_dir


def save_cache_dir(cache_dir):
    save_user_settings({
        'cache_dir': cache_dir
    })
