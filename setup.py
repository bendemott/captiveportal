"""
setup.py installation file for ``captiveportal``

For development see http://peak.telecommunity.com/DevCenter/setuptools#development-mode

Releasing
---------
To release a new version of the software.

    - Update the version number.
    - Test your changes by installing using ``sudo python setup.py install``
    - Commit your changes to the git repository hosting this code.
"""
__version__ = '0.4'
__application__ = 'captiveportal'

import os
import sys
try:
    from setuptools import setup
except ImportError:
    sys.stdout.write(os.linesep
        + 'NOTE: for --develop flag support execute ``pip install setuptools`` and run again'
        + os.linesep)
    from distutils import setup


REQUIRED_PYTHON_VERSION = (2, 6, 0)
README_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.rst'))
try:
    LONG_DESCRIPTION = open(README_PATH).read()
except Exception as e:
    sys.stderr.write("couldnt load README.rst - %s" % e)
    LONG_DESCRIPTION = ""

# Python Version Check
if sys.version_info < REQUIRED_PYTHON_VERSION:
    sys.stderr.write(
        '%s requires Python %s or greater' % (__application__, REQUIRED_PYTHON_VERSION.join('.')))
    sys.stderr.write(os.linesep)
    sys.exit(-1)
if sys.version_info >= (3,):
    sys.stderr.write('%s has not been tested with Python 3' % __application__)
    sys.stderr.write(os.linesep)
    sys.exit(-1)
    
setup(
    name=__application__,
    zip_safe=True, # ok to compress the source archive on disk
    version=__version__, 
    author='Ben DeMott',
    author_email='ben.demott@gmail.com',
    packages=[],
    url='https://github.com/bendemott/captiveportal',
    license='LICENSE',
    description='SpotOn Tablet Backend Server',
    long_description=LONG_DESCRIPTION,
    install_requires=[
        'Twisted >= 12.0', 
    ],
    # install these binary scripts
    scripts=['captiveportal'],
)
