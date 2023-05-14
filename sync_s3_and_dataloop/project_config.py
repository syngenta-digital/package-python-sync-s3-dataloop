import os
import boto3
import dtlpy as dl

class ProjectConfig:
    def __init__(self):

        dataloop_project = 'stand_count_bucket'
        dataloop_dataset = 'stand_count_bucket_data'

        self.bucket_name = 'protector-v4-static'
        self.bucket_folder_path = 'standcount/raw-images/'
    
        self.access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        self.secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

        self.project = dl.projects.get(project_name=dataloop_project)
        self.dataset = self.project.datasets.get(dataset_name=dataloop_dataset)

        self.s3 = boto3.client('s3', 
                            aws_access_key_id=self.access_key,
                            aws_secret_access_key=self.secret_key
                        )
