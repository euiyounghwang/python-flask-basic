#!/bin/bash

set -eu

SCRIPTDIR="$(
  cd -- "$(dirname "$0")" >/dev/null 2>&1
  pwd -P
)"

#--platform linux/amd64
# VS Code : Remove -it
docker run --rm -it --name euiyoung/fn-flask-basic-api-test --publish 15001:5000 --expose 5000 \
  -e DATABASE_URL=postgresql://postgres:1234@host.docker.internal:15432/postgres \
  -e ES_HOST=http://host.docker.internal:9203 \
  -e ES_LOGGER_INDEX=kafka_indexing \
  -e KAFKA_HOST=host.docker.internal:29092,host.docker.internal:39092 \
  -e KAFKA_TOPIC=test-topic,test1-topic \
  -v "$SCRIPTDIR:/app/FN-BEES-Services/" \
  euiyoung/fn-flask-basic-api:test
