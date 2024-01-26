#!/bin/bash
set -e

export PYTHONDONTWRITEBYTECODE=1

# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

source $SCRIPTDIR/.venv/bin/activate

# Start (flask run --no-reload)
# python main.py --debug run
gunicorn -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:5000" --log-level debug wsgi:app --reload

