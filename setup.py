"""prawcore setup.py."""

import re
from codecs import open
from os import path
from setuptools import setup


PACKAGE_NAME = 'prawcore'
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, 'const.py'),
          encoding='utf-8') as fp:
    VERSION = re.search("__version__ = '([^']+)'", fp.read()).group(1)


setup(name=PACKAGE_NAME,
      author='Bryce Boe',
      author_email='bbzbryce@gmail.com',
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython'),
      description='Low-level communication layer for PRAW 4+.',
      install_requires=['requests >=2.9.1, <3.0'],
      keywords='praw reddit api',
      license='Simplified BSD License',
      long_description=README,
      packages=[PACKAGE_NAME],
      tests_require=['betamax >=0.5.1, <0.6',
                     'betamax-serializers >=0.1.1, <0.2',
                     'mock >=1.3.0, <1.4'],
      test_suite='tests',
      url='https://github.com/praw-dev/prawcore',
      version=VERSION)
