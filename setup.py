#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from setuptools import setup
from pathlib import Path


def package_files(directory, *globs, match_filter="^$"):
    paths = []
    root = Path(directory)
    regex = re.compile(match_filter)
    for pattern in globs:
        files = root.glob(pattern)
        paths.extend(
            file.relative_to(root).as_posix()
            for file in files
            if file.is_file() and not regex.match(file.as_posix())
        )
    return {directory: paths}


setup(
    name="git-subrepo",
    version="0.4.1",
    description="Python package for installing git subrepo extension.",
    long_description="Python package for installing git subrepo extension.",
    author="Marcel Kuszak",
    author_email="marcel.kuszak@hella.com",
    license="MIT",
    url="https://github.com/ingydotnet/git-subrepo",
    platforms="any",
    # add single file module
    py_modules=["subrepo"],
    packages=["subrepo"],
    package_data=package_files(
        "subrepo",
        ".rc",
        "[A-Za-z]*",
        "lib/**/*",
        "ext/**/*",
        "man/**/*",
        "share/**/*",
        match_filter=r"(.*/test)",
    ),
    entry_points={"console_scripts": ["subrepo=subrepo:main"]},
    scripts=["activate_subrepo.bat", "activate_subrepo.sh"],
    include_package_data=True,
    # project dependencies for installation
    python_requires=">=3.6",
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    zip_safe=False,
    keywords="",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
