## Changes in 4.0.0

* Note: version 3 skipped in order to synchronize major version numbering
  with AVL user image.
* Update base image to v3.3.7, which provides jupyterhub package
  version 4.1.5.
* Update maintainer email address.
* Update avl package to version 0.3.0.
* Update boto3 to version 1.34.125.

## Changes in 2.0.0

* Update base image to v2.0.0 of jupyterhub-k8s-hub.
* Update agriculture-vlab package from 0.1.4 to 0.2.1.
* Install boto3 using pip, not apt.

## Changes in 1.1.3

* Update agriculture-vlab package from 0.1.3 to 0.1.4.

## Changes in 1.1.2

* Update agriculture-vlab package from 0.1.2 to 0.1.3.

## Changes in 1.1.1

* Update agriculture-vlab package from 0.1.1 to 0.1.2.

## Changes in 1.1.0

* Use k8s-hub:1.2.0 as the base image.

## Changes in 1.0.5

* Set `NB_USER`, not root, as default user for the image (fixes #1).
* Update base k8s-hub image to version 1.1.3-n460.h73387dcf, which provides
  version 2.2.0 of the jupyterhub package.

## Changes in 1.0.4

* Update agriculture-vlab package from 0.1.0 to 0.1.1.
