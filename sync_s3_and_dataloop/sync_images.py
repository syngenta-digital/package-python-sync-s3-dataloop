import boto3
import dtlpy as dl
import os

def save_image_on_dataloop(item_path, project_settings):
    response = project_settings.s3.get_object(Bucket=project_settings.bucket_name, Key=item_path)
    image = response['Body'].read()
    
    item_name = item_path.split('/')[-1]
    remote_path = item_path.replace('/'+item_name, '').replace('standcount/', '')

    project_settings.dataset.items.upload(local_path=image, remote_path=remote_path, remote_name=item_name, overwrite=True)

    return

def get_images_from_s3(project_settings):
    config = project_settings
    paginator = config.s3.get_paginator('list_objects_v2')
    result = paginator.paginate(Bucket=config.bucket_name, Prefix=config.bucket_folder_path)

    for page in result:
        if "Contents" in page:
            for obj in page["Contents"]:
                if ('.jpeg' in obj['Key']) or ('.jpg' in obj['Key']) or ('.png' in obj['Key']):
                    save_image_on_dataloop(obj['Key'], project_settings)