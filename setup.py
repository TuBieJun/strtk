import setuptools
import os
import sys
version_f = os.path.join(os.path.dirname(sys.argv[0]), "strtk/version.py")
with open(version_f) as f:
    exec(f.read())


setuptools.setup (
    name="strtk",
    version=__version__,
    author=__author__,
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
        "statsmodels"
    ]
)