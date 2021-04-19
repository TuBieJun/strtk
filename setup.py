import setuptools
import os
import sys


setuptools.setup (
    name="strtk",
    version="0.0.1",
    author="liteng",
    author_email="707704459@qq.com",
    description="Tools for string seq file",
    packages=setuptools.find_packages(),
    #url="https://github.com/wegene-llc/CNVar",
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
     entry_points={
        "console_scripts": [
            "strtk = strtk.main:main",
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        "statsmodels==0.12.0"
    ]
)