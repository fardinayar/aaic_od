_base_ = '../mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=8),
    )
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
