#!/bin/bash
set -e

export PYTHONDONTWRITEBYTECODE=1
# To Run the Server with Automatic Restart When Changes Occur

source ./read_config.sh

# --
# Call this function from './read_config.yaml.sh' to get ES_HOST value in config.yaml file
get_value_from_yaml
# --

# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# export FLASK_APP=$SCRIPTDIR/api/wsgi.py
# flask db init

source $SCRIPTDIR/.venv/bin/activate

# --
# Waitng for ES
./wait_for_es.sh $ES_HOST


# # Start (flask run --no-reload)
# python -m api.wsgi -e dev
# python -m api.wsgi -e prod
python -m api.wsgi -r API_AND_BACKGROUND -e dev
# python -m api.wsgi -r API_AND_BACKGROUND -e prod

# gunicorn -w 2 -b 0.0.0.0:5000 --reload api.wsgi
