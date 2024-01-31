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
  -e ES_HOST=http://host.docker.internal:9209 \
  -e ES_LOGGER_INDEX=kafka_indexing \
  -e KAFKA_HOST=host.docker.internal:29092,host.docker.internal:39092 \
  -e KAFKA_TOPIC=test-topic,test1-topic \
  -v "$SCRIPTDIR:/app/FN-BEES-Services/" \
  euiyoung/fn-flask-basic-api:es

