"""
    This module instructs the setuptools to setpup this package properly

    :copyright: (c) 2016 by Mehdy Khoshnoody.
    :license: GPLv3, see LICENSE for more details.
"""
import os
from distutils.core import setup

setup(
    name='pyeez',
    version='0.1.0',
    packages=['pyeez'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='terminal console',
    url='https://github.com/mehdy/pyeez',
    license='GPLv3',
    author='Mehdy Khoshnoody',
    author_email='me@mehdy.net',
    description='A micro-framework to create console-based applications like'
                'htop, vim and etc'
)
