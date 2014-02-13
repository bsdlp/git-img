try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Use GitHub to serve your images.',
    'author': 'Jon Chen',
    'url': 'https://github.com/fly/git-img',
    'download_url': 'https://github.com/fly/git-img/archive/0.0.1.tar.gz',
    'author_email': 'dabestmayne@burrito.sh',
    'version': '0.0.1',
    'install_requires': ['gitpython'],
    'packages': ['gitimg'],
    'scripts': ['gitimg'],
    'name': 'gitimg'
}

setup(**config)
