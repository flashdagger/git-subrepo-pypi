#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from setuptools import setup
from pathlib import Path


def description():
    readme_file = Path(__file__).with_name("README.md")
    long_description = readme_file.read_text("utf-8")
    return long_description


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
    version="0.4.3.post4",
    description="Python package for installing git subrepo extension.",
    long_description=description(),
    long_description_content_type="text/markdown",
    author="flashdagger",
    author_email="flashdagger@googlemail.com",
    license="MIT",
    url="https://github.com/flashdagger/git-subrepo-pypi",
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
    scripts=["git-subrepo-init" + suffix for suffix in (".bat", ".sh", ".ps1")],
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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
