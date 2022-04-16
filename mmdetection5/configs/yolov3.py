_base_ = '../mmdetection//configs/yolo/yolov3_d53_320_273e_coco.py'

load_from = 'checkpoints/yolov3_d53_320_273e_coco-421362b6 (1).pth'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(num_classes=8),
)

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('car', 'signal', 'signs', 'motorcycle', 'pedestrian', 'truck', 'bus', 'bicycle')
data = dict(
    train=dict(
        img_prefix='Dataset/images/train/',
        classes=classes,
        ann_file='Dataset/train.json'),
    test=dict(
        img_prefix='Dataset/images/test/',
        classes=classes,
        ann_file='Dataset/test.json'),
    )
