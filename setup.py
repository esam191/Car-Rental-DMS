try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'car_db',
    'author': 'Esam Uddin',
    'author_email': 'esam191@gmail.com',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'car_db'
}

setup(**config)
