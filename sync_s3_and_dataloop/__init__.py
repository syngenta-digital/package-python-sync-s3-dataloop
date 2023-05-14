#importado

from project_config import ProjectConfig
project_settings = ProjectConfig()

from dataloop_login import dl_login
from sync_images import get_images_from_s3
from sync_annotations import get_image_list_from_dl

sync_images_to_dataloop = get_images_from_s3
sync_annotations_to_dataloop = get_image_list_from_dl


