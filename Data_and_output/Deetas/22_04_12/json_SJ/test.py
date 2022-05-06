import sys
from typing import Dict
sys.path.append('../')

import json

# with를 이용해 파일을 연다.
file_path = "/home/dblab/maeng_space/dataset_2021/Deetas/data_22_04_12/json_MaskRCNN/segmentation_test.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    # print(json_data['annotations'][0]['image_id'])
    # print(json_data['images'][0]["file_name"])
    
    # list_G = []
    # for a in range(len(json_data['annotations'])):
    #     if json_data['annotations'][a]['image_id'] not in list_G:
    #         list_G.append(json_data['annotations'][a]['image_id'])
    # print(len(list_G))  # 141567 중 중복제거 후 28589
    # list_G2 = []
    # for v in list_G:
    #     if v not in list_G2:
    #         list_G2.append(v)
    # print(len(list_G2))   # 28589

    # list_R = []
    # for a in range(len(json_data['images'])):
    #     list_R.append(json_data['images'][a]["file_name"])
    # print(list_R)
    # print(len(list_R))  # 299919
    d = dict()
    for a in range(len(json_data['images'])):
        d[json_data['images'][a]['id']] = json_data['images'][a]["file_name"]
    print(d.items())
    # list_S = []
    # for a in range(len(json_data['images'])):
    #     list_R.append(json_data['images'][a]["file_name"])

    
# {"id": 336018, "license": 0, "file_name": "N-B-P-033_056989.jpg", "height": 1080, "width": 1920, "flickr_url": "", "coco_url": "", "date_captured": 0}], "annotations": [{"id": 881369, "image_id": 122283, "category_id": 6, "segmentation": [[176.15, 96.75, 296.74, 179.75, 508.16, 173.49, 501.89, 377.08, 501.89, 618.25, 508.16, 762.33, 263.85, 752.93, 165.19, 807.75, 146.39, 673.06, 138.56, 500.8, 141.7, 350.5, 151.09, 237.7]], "area": 215713.0, "bbox": [138.56, 96.75, 369.6, 711.0], "iscrowd": 0, "attributes": {"Status": "Opening", "occluded": false, "track_id": 231, "keyframe": true}}