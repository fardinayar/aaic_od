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

for annotation_path in glob('train/*.txt'):
    base_name = os.path.basename(annotation_path)
    image_name = base_name.replace('.txt', '.jpg')
    coco_image = CocoImage(file_name=image_name, height=HEIGHT, width=WIDTH)
    with open(annotation_path) as file:
        annotation_list = file.read().split("\n")
        annotation_list = [x.split(" ") for x in annotation_list]
        annotation_list = [[float(y) for y in x] for x in annotation_list]
        for line in annotation_list:
            details = line
            class_id = details[0]
            details[1] = float(details[1]- float(details[3]) / 2) * WIDTH
            details[2] = float(details[2]- float(details[4]) / 2) * HEIGHT
            details[3] = float(details[3]) * WIDTH
            details[4] = float(details[4]) * HEIGHT
            print(details)
            coco_image.add_annotation(CocoAnnotation(bbox=details[1:], category_id=int(class_id), category_name=categories[int(class_id)]))
    coco.add_image(coco_image)
save_json(coco.json, save_path='train.json')