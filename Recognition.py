import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import sys

import time

from Sorting_array import getArray,checkblob_Blue,checkblob_Pink

img = cv2.VideoCapture(0)
# cv2.flip(img, flipCode=-1)
# Setup SimpleBlobDetector parameters.
PARAMS = cv2.SimpleBlobDetector_Params()

# define range of blue color in HSV
# lowerBLUE = np.array([115, 100, 100])
# upperBLUE = np.array([130, 255, 255])

lowerBLUE = np.array([90, 100, 100])
upperBLUE = np.array([130, 255, 255])
# define range of pink color in HSV
lowerPINK = np.array([120, 100, 100])
upperPINK = np.array([180, 255, 255])

# lowerRED = np.array([100, 100, 100])
# upperRED = np.array([250, 255, 255])
count = 0
while True:

    # Take each frame
    _, frame = img.read()
    cropped = frame[200:500, 200:500]
    hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    maskBLUE = cv2.inRange(hsv, lowerBLUE, upperBLUE)

    # Bitwise-AND mask and original image
    resBLUE = cv2.bitwise_and(maskBLUE, maskBLUE,frame)

    mask1 = cv2.blur(maskBLUE, (7, 7), maskBLUE, (-1, -1), cv2.BORDER_DEFAULT)

    # Set up the detector with default parameters.
    detector2 = cv2.SimpleBlobDetector(PARAMS)

    # Detect blobs.
    reversemask = 180 - mask1
    keypointsBLUE = detector2.detect(reversemask)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints2 = cv2.drawKeypoints(mask1, keypointsBLUE, np.array([]), (0, 0, 0),
                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the resulting frame
    result1 = cv2.bitwise_and(cropped, im_with_keypoints2, mask=mask1)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.morphologyEx(result1, cv2.MORPH_CLOSE, kernel)
    # Set up the detector with default parameters.
    """--------------------------------------------------------------------------------------"""
    # Threshold the HSV image to get only pink colors
    maskPINK = cv2.inRange(hsv, lowerPINK, upperPINK)
    # maskRED = cv2.inRange(hsv, lowerRED, upperRED)

    MaskPR = maskPINK
    # Bitwise-AND mask and original image
    resPR = cv2.bitwise_and(frame, frame, MaskPR)

    mask2 = cv2.blur(MaskPR, (7, 7), MaskPR, (-1, -1), cv2.BORDER_DEFAULT)
    # Set up the detector with default parameters.
    detector2 = cv2.SimpleBlobDetector(PARAMS)

    # Detect blobs.
    reversemask2 = 180 - mask2
    keypointsPINK = detector2.detect(reversemask2)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints2 = cv2.drawKeypoints(mask2, keypointsPINK, np.array([]), (0, 0, 0),
                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the resulting frame
    result2 = cv2.bitwise_and(cropped, im_with_keypoints2, mask=mask2)
    kernel = np.ones((5, 5), np.uint8)
    dilation2 = cv2.morphologyEx(result2, cv2.MORPH_CLOSE, kernel)
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector(PARAMS)
    """---------------------------------------------------------"""

    cv2.imshow('detect blue', result1)
    cv2.imshow('detect red', result2)
    # if 5 ESC to exit
    k = cv2.waitKey(1) & 0xFF
    # if k == 27:
    #     break
    if k == ord(' '):
        break

cv2.destroyAllWindows()
#     time.sleep(0.5)
i = 0
coordiatesPINK = []
Prev_yPINK = 0
relevantXPINK = 0
max_yPINK = 0

arr_xPINK = []
arr_yPINK = []

for kpPINK in keypointsPINK:
    x = kpPINK.pt[0]
    y = kpPINK.pt[1]
    coordiatesPINK.append((round(x, 2), round(y, 2)))
    i = i + 1

    # plt.scatter(x, y)  # plot blue dots
    arr_xPINK.append(round(x, 2))
    arr_yPINK.append(round(y, 2))

    if Prev_yPINK == 0:
        Prev_yPINK = round(y, 2)
        max_yPINK = round(y, 2)
        relevantXPINK = round(x, 2)
    else:
        if y > Prev_yPINK:
            max_yPINK = round(y, 2)
            Prev_yPINK = round(y, 2)
            relevantXPINK = round(x, 2)
print "independent blob: ", relevantXPINK, ",", max_yPINK
print '\n', coordiatesPINK
# plt.scatter(arr_xPINK, arr_yPINK)
print '\n'"------pink------"
print "red blobs count = %d" % i

arr_Pink = []
dioganalSQRTPINK = 0
degreePINK = 0
for c in coordiatesPINK:
    c_x = c[0]
    c_y = c[1]
    dioganalSQRTPINK = math.pow((c_x - relevantXPINK), 2)+math.pow((c_y - max_yPINK), 2)
    distancePINK = math.sqrt(dioganalSQRTPINK)

    if distancePINK != 0:
        if c_x - relevantXPINK != 0:
            degreePINK = math.degrees(math.atan((c_y - max_yPINK)/(c_x - relevantXPINK)))
            arr_Pink.append((distancePINK, degreePINK, c_x))
    if distancePINK != 0:
        sys.stdout.write('(%f,%f) \t' % (c[0], c[1]))
        sys.stdout.write('%f \t' % distancePINK)
        sys.stdout.write('%f \n' % degreePINK)


# print "degerees pink",arr_degreesPINK
# getArray(arr_distancesPINK)
"""----------blue calculation-----------"""
j = 0
coordiatesBLUE = []

arr_xBLUE = []
arr_yBLUE = []

for kpBLUE in keypointsBLUE:
    x = kpBLUE.pt[0]
    y = kpBLUE.pt[1]
    coordiatesBLUE.append((round(x, 2), round(y, 2)))
    j = j + 1

    # plt.scatter(x, y)  # plot blue dots
    arr_xBLUE.append(round(x, 2))
    arr_yBLUE.append(round(y, 2))

print '\n'"------blue------"
print "Coordinates blue:", '\n', coordiatesBLUE
print "blue blobs count = %d" % j

dioganalSQRTBLUE = 0
degreeBLUE = 0
arr_BLUE = []

X_BLUE = []
for c in coordiatesBLUE:
    c_x = c[0]
    c_y = c[1]
    dioganalSQRTBLUE = math.pow((c_x - relevantXPINK), 2)+math.pow((c_y - max_yPINK), 2)
    distanceBLUE = math.sqrt(dioganalSQRTBLUE)

    if distanceBLUE != 0:
        X_BLUE.append((c_x, distanceBLUE))
        if c_x - relevantXPINK != 0:
            degreeBLUE = math.degrees(math.atan((c_y - max_yPINK)/(c_x - relevantXPINK)))
            degreeBLUE = round(degreeBLUE, 5)
            arr_BLUE.append((c_y,distanceBLUE,degreeBLUE,c_x))
    sys.stdout.write('(%f,%f) \t' % (c[0], c[1]))
    sys.stdout.write('%f \t' % distanceBLUE)
    sys.stdout.write('%f \n' % degreeBLUE)

print '\n'
plt.figure(1, figsize=(15, 5))
plt.subplot(121)
plt.plot(arr_xPINK, arr_yPINK, 'r', lw=0)
plt.scatter(arr_xPINK, arr_yPINK, s=50)
plt.title('Red')
# Scatter plot on top of lines
plt.subplot(122)
plt.plot(arr_xBLUE, arr_yBLUE, 'r', lw=0)
plt.scatter(arr_xBLUE, arr_yBLUE, s=50)
plt.title('blue')
plt.show()

middley = 0
temp_x = 0
if i != 0:
    for item in arr_Pink:
        checkblob_Pink(item[0], item[1], item[2], temp_x)
        temp_x = item[2]

if j != 0:
    sortYBlue = getArray(arr_BLUE)
    for item in arr_BLUE:
        middley = (sortYBlue[sortYBlue.__len__()-1][0]+sortYBlue[0][0])/2
        checkblob_Blue(middley, item[0], item[1], item[2])


print "Middle: ",middley
from Sorting_array import print_blob_array
print_blob_array()
#  k = cv2.waitKey(1) & 0xFF
#     # if k == 27:
#     #     break
#     if k == ord(' '):
#         break
#
# cv2.destroyAllWindows()
