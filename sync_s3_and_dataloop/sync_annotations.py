import boto3
import dtlpy as dl
import os
import json

def get_annotations_from_s3(items_list, configs):
    for item in items_list:
        file_path = os.path.dirname(item['file_path'])
        file_path = ('standcount'+ file_path)

        try:
            response = configs.s3.get_object(Bucket=configs.bucket_name, Key=os.path.join(file_path, 'after_edit.json'))
        except:
            response = configs.s3.get_object(Bucket=configs.bucket_name, Key=os.path.join(file_path, 'before_edit.json'))

        annotation = response['Body'].read()
        annotation = annotation.decode('utf-8')
        json_annotation = json.loads(annotation)
        bboxes_list = []
        bboxes = json_annotation['mosaic']['positions']
        
        item = configs.dataset.items.get(item_id=item['item_dataloop_id'])
        builder = item.annotations.builder()
        for bbox in bboxes:
            bboxes_dict = {}
            if bbox['deleted'] == False:
                builder.add(annotation_definition=dl.Box(
                                                        top=bbox['top'],
                                                        left=bbox['left'],
                                                        bottom=bbox['top'] + bbox['height'],
                                                        right=bbox['left'] + bbox['width'],
                                                        label='plant'
                                                        )
                            )
        item.annotations.upload(builder)


def get_image_list_from_dl(project_settings):
    
    dataloop_images_list = []
    
    dataset = project_settings.dataset
    
    pages = dataset.items.list()
    for page in pages:
        for item in page:
            item_data = {}
            item_data['file_path'] = item.filename
            item_data['item_dataloop_id'] = item.id
            dataloop_images_list.append(item_data)

    get_annotations_from_s3(dataloop_images_list, project_settings)
