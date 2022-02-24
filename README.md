# Agriculture Virtual Laboratory custom JupyterHub hub image

We maintain our own image for the hub container, based closely on
the standard "Zero to JupyterHub with Kubernetes" image from the
<https://hub.docker.com/r/jupyterhub/k8s-hub> repository, defined
in
<https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/main/images/hub>.
In our custom image, we modify the standard image as follows:

1. Install the python3-boto3 package.

2. Add a `agriculturevlab.create_user` Python module to the environment,
   which can be used to create temporary IAM users on login to give the
   AVL user access to the AVL S3 user bucket.
