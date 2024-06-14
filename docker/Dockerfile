# We use a standard JupyterHub hub image as base. Unlike the user image,
# the hub image is not intended for (much) customization, so we make as few
# changes as possible.

# As of 2024, JupyterHub images are now available on quay.io, so we no longer
# have to duplicate them from dockerhub to work around the issue described at
# https://issues.redhat.com/browse/PROJQUAY-1299. The base images are defined
# at https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/main/images/hub.

# The base image version should be chosen carefully for compatibility with
# the z2jh Helm chart and the user image.

FROM quay.io/jupyterhub/k8s-hub:3.3.7

# The parent image sets NB_USER as an ARG, not an ENV, so we have to
# set it explicitly here.
ARG NB_USER=jovyan

LABEL maintainer="contact@agriculturevlab.eu"
LABEL name="avl-jh-hub"
LABEL version="4.0.0"
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
#   than apt, because pip puts it in site-packages where python can find it.
# - We temporarily install gcc and libc-dev because pip needs them to install
#   the avl package from its tarball.

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --yes \
    && apt-get install --yes --no-install-recommends gcc libc-dev \
    && pip install boto3==1.34.125 \
    && pip install --no-deps \
    https://github.com/agriculture-vlab/agriculture-vlab/archive/refs/tags/v0.3.0.tar.gz \
    && pip cache purge \
    && apt-get purge --yes gcc libc-dev \
    && apt-get autoremove --yes \
    && apt-get clean --yes \
    && rm -rf /var/lib/apt/lists/*

# Use NB_USER as the default user when executing the image.
USER ${NB_USER}
