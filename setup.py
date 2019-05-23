#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Pyson AgentSpeak interpreter.
# Copyright (C) 2016 Niklas Fiekas <niklas.fiekas@tu-clausthal.de>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import setuptools
import sys


def read_description():
    with open('README.rst') as readme_file:
        readme = readme_file.read()

    with open('HISTORY.rst') as history_file:
        history = history_file.read()

    return readme + '\n\n' + history


def dependencies():
    deps = ["colorama"]

    if sys.version_info < (3, 4):
        deps.append("enum34")

    return deps


setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setuptools.setup(
    name="agentspeak",
    version="0.0.1",
    author="Niklas Fiekas",
    author_email="niklas.fiekas@tu-clausthal.de",
    description="JASON-style AgentSpeak for Python.",
    long_description=read_description(),
    license="GPL3",
    keywords="jason multi agent simulation agent-speak",
    url="https://github.com/niklasf/python-agentspeak",
    packages=["agentspeak"],
    install_requires=dependencies(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 2- Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Other",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Libraries",
    ],
)
