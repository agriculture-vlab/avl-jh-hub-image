# We use a standard JupyterHub hub image as base. The original image is hosted
# on Docker Hub, but we use our own copy on quay.io, because Docker Hub's
# anonymous pull rate limits and quay.io's lack of support for pull
# credentials cause Docker-Hub-based builds to fail on quay.io; see
# https://issues.redhat.com/browse/PROJQUAY-1299?_sscc=t for details.

FROM quay.io/bcdev/jupyterhub:2.1.1

LABEL maintainer="pontus.lurcock@brockmann-consult.de"
LABEL name="avl-jh-hub"
LABEL version="1.0.0"
LABEL description="AVL JupyterHub hub image"

USER root


# Install boto3

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    python3-boto3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add create user module

COPY create_user.py /usr/local/lib/python3.8/dist-packages/agriculturevlab/create_user.py

WORKDIR "${HOME}"