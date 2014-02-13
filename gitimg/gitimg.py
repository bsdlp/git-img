#!/usr/bin/env python2

import ConfigParser
import os

class config_opts(object):
    """
    Config stuffs are saved here.
    """

    def __init__(self, gitimg_path=None):
        self.gitimg_path = gitimg_path


def get_config():
    """
    Look for configuration and parse it for the gitimg path. Return True and
    store value in config_opts if found, else return False.
    """

    gitimg_path = None

    if 'GITIMG_PATH' in os.environ:
        config_paths = [os.environ['GITIMG_PATH']]
    else:
        paths = ['~/.gitimg']

    paths = [os.path.expandvars(p) for p in paths]
    paths = [os.path.expanduser(p) for p in paths]

    cfg = ConfigParser.RawConfigParser()
    cfg.read(paths)

    if 'GITIMG_PATH' in os.environ:
        gitimg_path = os.environ['GITIMG_PATH']
    elif cfg.has_section('GITIMG'):
        gitimg_path = cfg.get('GITIMG', 'path')

    if gitimg_path:
        config_opts(gitimg_path)
        return True
    else:
        return False

