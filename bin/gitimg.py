#!/usr/bin/env python2

import config
import git

repo = git.Repo(config.GITIMG_PATH)
assert repo.bare == False

