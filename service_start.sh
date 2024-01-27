#!/bin/bash
set -e

# export PYTHONDONTWRITEBYTECODE=1

# To Run the Server with Automatic Restart When Changes Occur

# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

source $SCRIPTDIR/.venv/bin/activate

# Start (flask run --no-reload)
# gunicorn -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:5000" --log-level debug wsgi:app --reload
# gunicorn -k uvicorn.workers.UvicornWorker -w 2 --bind "0.0.0.0:5000" api.wsgi
gunicorn -w 1 -b 0.0.0.0:5000 --reload api.wsgi