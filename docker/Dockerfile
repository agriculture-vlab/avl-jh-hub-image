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

FROM quay.io/bcdev/jupyterhub-k8s-hub:2.0.0

# The parent image sets NB_USER as an ARG, not an ENV, so we have to
# set it explicitly here.
ARG NB_USER=jovyan

LABEL maintainer="pontus.lurcock@brockmann-consult.de"
LABEL name="avl-jh-hub"
LABEL version="2.0.0-beta.1"
LABEL description="AVL JupyterHub hub image"

USER root

# Install AVL package.
#
# - We don't need conda or the full avl dependencies, so we use --no-deps when
#   installing avl and instead explicitly install boto3, which is the only
#   dependency that the _admin module needs.
# - As of v2.0.0, the k8s hub image we use as base is in turn based on the
#   Debian-based official Python image, which doesn't include dist-packages
#   in the Python path. So it's simplest to install boto3 with pip rather
#   than apt, which puts it in site-packages where python can find it.
# - We temporarily install gcc and libc-dev because pip needs them to install
#   the avl package from its tarball.

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --yes \
    && apt-get install --yes --no-install-recommends gcc libc-dev \
    && pip install boto3==1.26.41 \
    && pip install --no-deps \
    https://github.com/agriculture-vlab/agriculture-vlab/archive/refs/tags/v0.1.4.tar.gz \
    && pip cache purge \
    && apt-get purge --yes gcc libc-dev \
    && apt-get autoremove --yes \
    && apt-get clean --yes \
    && rm -rf /var/lib/apt/lists/*

# Use NB_USER as the default user when executing the image.
USER ${NB_USER}
