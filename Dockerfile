
FROM --platform=linux/amd64 python:3.6.13 as environment
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app
ENV CONDA_NUMBER_CHANNEL_NOTICES=0

RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh
RUN bash Miniconda3-4.7.12.1-Linux-x86_64.sh -b -p conda

RUN conda/bin/conda install \
    # Install boto3 to use our S3 channel
    boto3
RUN echo 'conda ==4.7.12' > /app/conda/conda-meta/pinned

COPY requirements.txt deps/requirements.txt
# COPY test-requirements.txt deps/test-requirements.txt

# Create environment
RUN conda/bin/conda create --yes --quiet --name fn_bees_services && \
    /bin/bash -c 'source /app/conda/bin/activate fn_bees_services && \
    #    PKG_VERSION=git pip install setuptools==43.0.0 && \
    #    pip install --user pytest-runner==5.2 && \
    pip install --upgrade pip && \
    # pip install --no-cache-dir -r deps/test-requirements.txt && \
    pip install --no-cache-dir -r deps/requirements.txt'




# Create runtime image
FROM --platform=linux/amd64 python:3.6.13 as runtime

WORKDIR /app
COPY --from=environment /app .
COPY . FN-BEES-Services


RUN /bin/bash -c 'source /app/conda/bin/activate fn_bees_services && \
    pip install --upgrade pip && \
    # pip install --no-cache-dir -r deps/test-requirements.txt && \
    pip install --no-cache-dir -r deps/requirements.txt'


RUN useradd deploy
#COPY config.yaml .fn_rabbit.json logging.yaml /app/FN-BEES-Services/
RUN chown -R deploy: /app/conda/envs/fn_bees_services /app/FN-BEES-Services

RUN mkdir -p /home/deploy/fn_services_logs && \
    chown -R deploy: /home/deploy/fn_services_logs/

# Need these two lines to install VSCode extensions in devcontainer
RUN mkdir -p /home/deploy/
RUN chown -R deploy: /home/deploy

USER deploy


ENTRYPOINT ["/app/FN-BEES-Services/conda-run-entrypoint.sh"]

