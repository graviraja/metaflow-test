#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "metaflow_test"
DESCRIPTION = "Metaflow meta-test"
URL = ""
EMAIL = ""
AUTHOR = ""
INSTALL_PACKAGES = []

here = os.path.abspath(os.path.dirname(__file__))


# Load the package's __version__.py module as a dictionary.
about = {"__version__": "0.1.0"}

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=("tests", "notebooks", "data")),
    test_suite="tests",
    include_package_data=True,
    zip_safe=False,  # the package can run out of an .egg file
    install_requires=INSTALL_PACKAGES,
)
