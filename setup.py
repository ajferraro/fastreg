try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fastreg',
    'author': 'Angus Ferraro',
    'version': '0.1',
    'packages': ['fastreg'],
    'name': 'fastreg'
}

setup(**config)
