#!/bin/bash
set -e

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

function make_python_virtual_env() {
    # Create virtualenv
    python -m venv $SCRIPTDIR/.venv
    
    source $SCRIPTDIR/.venv/bin/activate
    echo "Created virtual enviroment >>" + $SCRIPTDIR/.venv/bin/activate
    
    echo "Install requirements.txt"
    pip install --upgrade pip
    pip install -r $SCRIPTDIR/requirements.txt
    echo "Install Completely.."
}

if [ -d $SCRIPTDIR/.venv ]; then
  echo "Directory exists."
  rm -rf $SCRIPTDIR/.venv
fi

make_python_virtual_env


