#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

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
    packages=["subrepo"],
    # package_dir={project: project},
    entry_points={
        "console_scripts": [
            "subrepo=subrepo:main",
        ]
    },
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
