"""
Copyright 2019-2020 (c)iON|UL.com. All rights reserved.

Description: Setup for driver pkg.
"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='ds_driver',
    version='0.3.0',
    description="An Ion package to serve data science models.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "fasttext>=0.8.3",
        "future>=0.17.1",
        "joblib>=0.14.1",
        "spacy>=2.2.3",
        "pandas>=0.25.3",
        "pyod==0.7.5",
        "pyyaml>=5.1.1",
        "xgboost>=0.90",
        "networkx>=2.2",
        "nltk>=3.4.5",
        "numpy>=1.17.1",
        "scikit-learn>=0.20.3",
        "scipy>=1.3.1",
        "six>=1.12.0"
    ]
)
