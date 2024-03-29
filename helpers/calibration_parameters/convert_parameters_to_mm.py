import numpy as np
import cv2

"""
INPUT
cameraMatrix Input 3x3 camera matrix that can be estimated by cv.calibrateCamera or cv.stereoCalibrate.
imageSize Input image size [w,h] in pixels.
apertureWidth Physical width in mm of the sensor.
apertureHeight Physical height in mm of the sensor

OUTPUT
S Struct with the following fields:
    fovx Output field of view in degrees along the horizontal sensor axis.
    fovy Output field of view in degrees along the vertical sensor axis.
    focalLength Focal length of the lens in mm.
    principalPoint Principal point [cx,cy] in mm.
    aspectRatio Pixel aspect ratio fy/fx.

"""

cameraMatrix = np.load("/helpers/calibration_parameters/phantom/parameter_05/matrix.npy")
imageSize = [2736, 1824]
apertureWidth = 13.5
apertureHeight = 8.8
s = cv2.calibrationMatrixValues(cameraMatrix, imageSize, apertureWidth, apertureHeight)


print(s)