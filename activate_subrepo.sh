#!/usr/bin/env bash

CUR_FILE="${BASH_SOURCE[${#BASH_SOURCE[@]} - 1]}"

if [ -z "$PS1" ] ; then
    echo "This script must be sourced. Use \"source ${CUR_FILE}\" instead."
    exit
fi

module_path=$(python -c "import subrepo; print(subrepo.__file__)")
subrepo_dir="$(dirname $(realpath -s $module_path))/subrepo"
source "$subrepo_dir/.rc"
version=$(git subrepo --version)
echo using version $version in $subrepo_dir
