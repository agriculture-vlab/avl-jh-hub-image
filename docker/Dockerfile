# We use a standard JupyterHub hub image as base. The original image is hosted
# on Docker Hub, but we use our own copy on quay.io, because Docker Hub's
# anonymous pull rate limits and quay.io's lack of support for pull
# credentials cause Docker-Hub-based builds to fail on quay.io; see
# https://issues.redhat.com/browse/PROJQUAY-1299?_sscc=t for details.
# The base image is copied from https://hub.docker.com/r/jupyterhub/k8s-hub
# and defined in
# https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/main/images/hub .
# The base image version should be chosen carefully for compatibility with
# the z2jh Helm chart and the user image.

FROM quay.io/bcdev/jupyterhub-k8s-hub:1.2.0

# The parent image sets NB_USER as an ARG, not an ENV, so we have to
# set it explicitly here.
ARG NB_USER=jovyan

LABEL maintainer="pontus.lurcock@brockmann-consult.de"
LABEL name="avl-jh-hub"
LABEL version="1.1.1"
LABEL description="AVL JupyterHub hub image"

USER root

# Install boto3
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    python3-boto3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install AVL package. Note the use of --no-deps: for the hub, we only need
# the avl._admin module, which doesn't have any dependencies beyond boto3
# and standard library modules. So we don't set up a whole conda environment
# here, but just install AVL for the system Python which is used to run the
# jupyterhub process.
RUN python3 -m pip install --no-deps \
    https://github.com/agriculture-vlab/agriculture-vlab/archive/refs/tags/v0.1.2.tar.gz

# Use NB_USER as the default user when executing the image.
USER ${NB_USER}
