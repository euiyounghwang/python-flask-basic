#!/bin/bash

set -eu

SCRIPTDIR="$(
  cd -- "$(dirname "$0")" >/dev/null 2>&1
  pwd -P
)"


docker run --rm --platform linux/amd64 -it -d \
  --name fn-flask-basic-pi --publish 15000:5000 --expose 5000 \
  --network bridge \
  -e DATABASE_URL=postgresql://postgres:1234@host.docker.internal:15432/postgres \
  -v "$SCRIPTDIR:/app/FN-BEES-Services/" \
  fn-flask-basic-api:es

