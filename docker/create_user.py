#!/usr/bin/env python3

"""Create a temporary IAM user for AVL user bucket access

This module provides a function create_user, which uses a user manager IAM
account to create a temporary user account allowing access to a single prefix
of the AVL user bucket, analogous to a home directory. The user IAM account is
temporary in the sense that it's not expected to persist between user
sessions, but it does not delete itself automatically -- unused accounts need
to be cleaned up actively, e.g. by regularly running a culler process to
delete any accounts not associated with an activate AVL session.
"""


import boto3
import os
import sys
from typing import Tuple
import json


def main():
    print(create_user(sys.argv[1]))


def create_user(user_name: str) -> Tuple[str, str]:
    client = boto3.client(
        service_name="iam",
        region_name="eu-central-1",
        aws_access_key_id=os.environ["USER_MANAGER_CLIENT_ID"],
        aws_secret_access_key=os.environ["USER_MANAGER_CLIENT_SECRET"]
    )
    iam_user_name = f"avlbu-{user_name}"
    try:
        user = client.create_user(
            Path="/avl-bucket-user/",
            UserName=iam_user_name,
            PermissionsBoundary=os.environ["BUCKET_USER_PERMISSIONS_BOUNDARY"]
        )
    except client.exceptions.EntityAlreadyExistsException:
        print("User exists; creating new credentials for existing user.")
    add_policy(client, user_name, iam_user_name)
    user_key_id, user_key_secret = create_access_key(client, iam_user_name)

    os.environ["BUCKET_USER_ACCESS_KEY_ID"] = user_key_id
    os.environ["BUCKET_USER_ACCESS_KEY_SECRET"] = user_key_secret
    return user_key_id, user_key_secret


def create_access_key(client, iam_user_name):
    user_key = client.create_access_key(UserName=iam_user_name)
    user_key_id = user_key["AccessKey"]["AccessKeyId"]
    user_key_secret = user_key["AccessKey"]["SecretAccessKey"]
    return user_key_id, user_key_secret
    

def add_policy(client, user_name, iam_user_name):
    policy = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowList",
                "Effect": "Allow",
                "Action": [ "s3:ListBucket" ],
                "Resource": [
                    "arn:aws:s3:::agriculture-vlab-user",
                    f"arn:aws:s3:::agriculture-vlab-user/{user_name}",
                    f"arn:aws:s3:::agriculture-vlab-user/{user_name}/*"
                ],
                "Condition": {
                    "ForAllValues:StringLike": {
                        "s3:prefix": [ f"{user_name}/", f"{user_name}/*" ]
                    }
                }
            },
            {
                "Sid": "AllowSomeOperations",
                "Effect": "Allow",
                "Action": [
                    "s3:AbortMultipartUpload",
                    "s3:ListMultipartUploadParts",
                    "s3:DeleteObject*",
                    "s3:GetObject*",
                    "s3:PutObject*"
                ],
                "Resource": [
                    f"arn:aws:s3:::agriculture-vlab-user/{user_name}",
                    f"arn:aws:s3:::agriculture-vlab-user/{user_name}/*"
                ]
            }
        ]
    })
    client.put_user_policy(
        UserName=iam_user_name,
        PolicyName="policy1",
        PolicyDocument=policy
    )


if __name__ == "__main__":
    main()
