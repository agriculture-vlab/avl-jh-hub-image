# Agriculture Virtual Laboratory custom JupyterHub hub image

We maintain our own image for the hub container, based closely on
the standard "Zero to JupyterHub with Kubernetes" image from the
<https://hub.docker.com/r/jupyterhub/k8s-hub> repository, defined
in
<https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/main/images/hub>.
In our custom image, we modify the standard image as follows:

1. Install the python3-boto3 package.

2. Install the `avl` package, which provides facilities to create temporary IAM
   users on login to give the AVL user access to the AVL S3 user bucket.

The `avl` package is only installed for the user management utilities provided
by its `_admin` module. The full dependencies of the `avl` package are *not*
installed, so functionality from other `avl` modules may not be available in
this image.

## jupyterhub package versioning

The Jupyter hub process and single-user notebook server communicate using
an API provided by the `jupyterhub` package. For reliable operation, the hub and
user images in a deployment must use the same minor version of this package. You
can check the `jupyterhub` version in the hub image with the following command:

```bash
docker run -it --rm quay.io/bcdev/avl-hub:<tag> \
    python3 -c 'import jupyterhub; print(jupyterhub.__version__)'
```
