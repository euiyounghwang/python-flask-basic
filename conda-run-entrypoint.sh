#!/bin/bash
set -ex

#. /app/conda/bin/activate fn_bees_services
source /app/conda/bin/activate fn_bees_services
cd /app/FN-BEES-Services
exec gunicorn -w 2 -b 0.0.0.0:5000 api.wsgi