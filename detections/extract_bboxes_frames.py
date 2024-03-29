import csv
import os
import cv2
import numpy as np
import pandas as pd
from performance.bounding_boxes import BoundingBoxes
from detections.yolo_predictions import YoloPredictions

save_path = '/home/ellentuane/Documents/IC/yolov4_obj_detection/Detections/extracted_bbox'
frames = '/home/ellentuane/Documents/IC/yolov4_obj_detection/Detections/frames'
classes_path = '/home/ellentuane/Documents/IC/yolov4_obj_detection/Detections/classes/coco.names'
cfg_path = '/home/ellentuane/Documents/IC/yolov4_obj_detection/Detections/cfg/yolov4-tiny.cfg'
weight_path = '/home/ellentuane/Documents/IC/yolov4_obj_detection/Detections/weights/yolov4-tiny.weights'

# .names files with the object's names
labels = open(classes_path).read().strip().split('\n')

# Random colors for each object category
colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

# yolo weights and cfg configuration files
net = cv2.dnn.readNetFromDarknet(cfg_path, weight_path)

use_gpu = 0
if use_gpu == 1:
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Obter o nome das categorias
layer_names = YoloPredictions.layer_name(net)

i = 0

while i < len(os.listdir(frames)):
    for frame in os.listdir(frames):
        data = []
        image_name = frame.split(".")[0]

        image = cv2.imread(os.path.join(frames, frame))

        if not image is None:

            # net, layer_names, image, confidence, threshold, net_height, net_width
            boxes, confidences, classIDs, idxs = YoloPredictions.make_prediction(net, layer_names, image,
                                                                                     0.01, 0.03, 960, 960)
            for class_id, score, bbox, idx in zip(classIDs, confidences, boxes, idxs):
                x, y, w, h = bbox
                class_name = labels[class_id]
                if class_name == 'person':
                    #data.append([x, y, w, h])
                    data.append([class_name, int(score * 100), x, y, w, h])
                    #frame = BoundingBoxes.draw_bounding_boxes(image, class_name, boxes, confidences, classIDs, idxs, colors)
                else:
                    pass
            #df = pd.DataFrame(data, columns=['class_name', 'score', 'x', 'y', 'w', 'h'])
            #df.to_csv(f"{save_path}/{image_name}.csv", index=False)

            with open(f"{save_path}/{image_name}_416.txt", 'w') as f:
                for line in data:
                    #f.write(str(line))
                    f.write('%s\n' % line)
                    f.write('\n')
        else:
            print('Image has ended, failed or wrong path was given.')
            break
    i += 1
    print(i)
cv2.destroyAllWindows()
