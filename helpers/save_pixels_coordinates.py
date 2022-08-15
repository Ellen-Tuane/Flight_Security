import os
import cv2
import pandas as pd

data_path = '/home/ellentuane/Documents/IC/Flight Security/detections/frames/10'
output_path = '/home/ellentuane/Documents/IC/Flight Security/detections/frames/'


def click_event(event, x, y, flags, params):
    # function to display the pixel coordinates
    # of the points clicked on the image
    global ix, iy
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y


# driver function
if __name__ == "__main__":
    i = 1
    geo_reference = []

    # loading images
    for frame in os.listdir(data_path):
        ix, iy = [], []

        # remove .jpg or any image type from image name
        image_name = frame.split(".")[0]
        image = cv2.imread(os.path.join(data_path, frame))

        if not image is None:
            height, width = image.shape[:2]
            cv2.namedWindow(f'{image_name}', cv2.WINDOW_NORMAL)
            cv2.resizeWindow(f'{image_name}', width, height)
            cv2.setMouseCallback(f'{image_name}', click_event)
            #print('fora da funcao', ix, iy)
            cv2.imshow(f'{image_name}', image)
            cv2.waitKey(3000) & 0xFF
            #print('fora da funcao2', ix, iy)
            geo_reference.append([image_name, ix, iy])
            print(i, 'of', len(os.listdir(data_path)), 'images')

            i += 1
    df = pd.DataFrame(geo_reference, columns=['image_name', "pixel_x", "pixel_y"])
    df.to_csv(f"{output_path}/real_distance_10m.csv", index=False)