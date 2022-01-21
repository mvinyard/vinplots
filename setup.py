from setuptools import setup
import re, os, sys

setup(
    name="vinplots",
    version="0.0.1",
    python_requires=">3.7.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url="https://github.com/mvinyard/vinplots",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="crispr_tools - Analysis Tools for CRISPR Screen Design and Analysis",
    packages=[
        "vinplots",
    ],
    install_requires=[
        "matplotlib>=3.4",
        "numpy>=1.19.2",
        "pandas>=1.1.2",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
