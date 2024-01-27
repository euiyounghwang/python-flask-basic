#!/bin/bash

set -eu

#docker build \
#  -f "$(dirname "$0")/Dockerfile" \
#  -t fn-bees-omnisearch:es \
#  --target es \
#  "$(dirname "$0")/."

#docker build --no-cache \

# docker build \
#   -f "$(dirname "$0")/Dockerfile" \
#   -t fn-bees-omnisearch:omni_es \
#   --target omni_es \
#   "$(dirname "$0")/."

# docker build \
#   -f "$(dirname "$0")/Dockerfile" \
#   -t fn-flask-basic-api:test \
#   --target test \
#   "$(dirname "$0")/."

docker build \
  -f "$(dirname "$0")/Dockerfile" \
  -t euiyoung/fn-flask-basic-api:es \
  --target runtime \
  "$(dirname "$0")/."


