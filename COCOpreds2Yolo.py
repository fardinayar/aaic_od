import glob
import json
#GT
json_test = open('test.json')
test_str = json_test.read()
test_data = json.loads(test_str)
#preds
json_pred = open('i.bbox.json')
pred_str = json_pred.read()
pred_data = json.loads(pred_str)
H=1280
W=1920

for image in test_data['images']:
    image_id = image['id']
    image_name = image['file_name']
    f = open(f"preds/{image_name.replace('.jpg','.txt')}", "w")
    for anno in pred_data:
        if anno['image_id'] == image_id:
            bbox = anno['bbox']
            bbox[0] += bbox[2]/2
            bbox[1] += bbox[3]/2
            bbox[0] /= W
            bbox[2] /= W
            bbox[1] /= H
            bbox[3] /= H
            class_id = anno['category_id']
            score = anno['score']
            f.write(f'{class_id} {score} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n')
    f.close()


for file in glob.glob('preds/*.txt'):
    with open(file) as f:
        lines = f.read().rstrip('\n')

    with open(file, 'w') as f:
        f.write(lines)
    f.close()
