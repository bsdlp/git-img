try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'author': 'Jon Chen',
    'author_email': 'dabestmayne@burrito.sh',
    'description': 'Use GitHub to serve your images.',
    'download_url': 'https://github.com/fly/git-img/archive/0.0.1.tar.gz',
    'install_requires': ['gitpython'],
    'long_description': open('README.md', 'rt').read(),
    'name': 'gitimg',
    'packages': ['gitimg'],
    'scripts': ['gitimg'],
    'url': 'https://github.com/fly/git-img',
    'version': '0.0.1',
}

setup(**config)
