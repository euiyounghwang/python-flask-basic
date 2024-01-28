#!/bin/bash
set -e

source /app/conda/bin/activate fn_bees_services
cd /app/FN-BEES-Services
python -m py.test -v ./tests --disable-warnings