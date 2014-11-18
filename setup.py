#!/usr/bin/env python


PROJECT = 'kaggle-cli'
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='An unofficial Kaggle command line tool.',
    long_description=long_description,

    author='floydsoft',
    author_email='floydsoft@gmail.com',

    url='https://github.com/floydsoft/kaggle-cli',
    download_url='https://github.com/floydsoft/kaggle-cli/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff', 'mechanize', 'lxml'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'kg = kaggle_cli.main:main'
        ],
        'kaggle_cli': [
            'submit = kaggle_cli.submit:Entry'
        ],
    },

    zip_safe=False,
)