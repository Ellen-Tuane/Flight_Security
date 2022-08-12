import os.path
import datetime
import os
import cv2
import pandas as pd

save_path = '/home/ellentuane/Documents/IC/output_confusion_matriz/city'
dir_img = '/home/ellentuane/Documents/IC/imagens_nivaldo/all/'

name = []
time = []
for frame in os.listdir(dir_img):
    image_name = frame
    name.append(frame)
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(dir_img, image_name)))
    time.append(modified_time)

    print(image_name, modified_time)

data = {'img_name': name, 'date_time':time}
df = pd.DataFrame(data)
df.to_csv('img_date_time.csv')

