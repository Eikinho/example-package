#!/usr/bin/env python3

from setuptools import setup

setup(name='dev_aberto_eikily',
      version='0.1',
      packages=['dev_aberto'],
      install_requires = ['requests'],
      scripts=["scripts/hello.py"]
      )