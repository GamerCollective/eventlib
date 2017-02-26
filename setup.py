#!/usr/bin/env python

from distutils.core import setup

setup(
    name='eventlib',
    version='0.1.0',
    description='Event library',
    author='Ian Auld',
    author_email='imauld@gmail.com',
    url="https://github.com/GamerCollective/eventlib",
    packages=[
        "distutils",
        "distutils.command",
        "redis"
    ],
)
