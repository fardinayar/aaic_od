import matplotlib.pyplot as plt
#pip install sahi
from sahi.utils.coco import Coco, CocoCategory, CocoImage, CocoAnnotation
from sahi.utils.file import save_json
from glob import glob
import os

coco = Coco()

categories = ['car', 'signal', 'signs', 'motorcycle', 'pedestrian', 'truck', 'bus', 'bicycle']
HEIGHT = 1280
WIDTH = 1920

for id, cat in enumerate(categories):
    coco.add_category(CocoCategory(id=id, name=cat))

for annotation_path in glob('test/*.txt'):
    base_name = os.path.basename(annotation_path)
    image_name = base_name.replace('.txt', '.jpg')
    coco_image = CocoImage(file_name=image_name, height=HEIGHT, width=WIDTH)
    coco.add_image(coco_image)
save_json(coco.json, save_path='test.json')