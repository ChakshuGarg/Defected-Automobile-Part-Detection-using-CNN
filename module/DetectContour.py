import numpy as np
import argparse
import glob
import cv2
import math
import matplotlib.pyplot as plt
from skimage import measure
from skimage.measure import label, regionprops
from PIL import Image
import skimage
import matplotlib.pyplot as plt

'''imagepath="D:/JBM/YE358311_Fender_apron/YE358311_defects/IMG20180905150336.jpg"
image = cv2.imread(imagepath)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([122,35,122], dtype = "uint8")
upper = np.array([124,37,224], dtype = "uint8")
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
plt.imshow(output)   # this colormap will display in black / white
plt.show()

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged


 

for imagePath in glob.glob(imagepath):
	# load the image, convert it to grayscale, and blur it slightly
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (3, 3), 0)
 
	auto = auto_canny(blurred)
 
	cv2.imshow("Original", image)
	cv2.imshow("Edges", np.hstack([auto]))
	cv2.waitKey(0)

'''
def FindContours(image):    
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = measure.find_contours(image, 25,fully_connected='high', positive_orientation='high')
    return contours


image = cv2.imread("C:/Users/Administrator/Desktop/JBM/blackedEdge.JPG")
height, width, channels = image.shape
blackBackground = np.zeros((height, width, channels), np.uint8)
contours=FindContours(image)
largest_area=0
for i,contour in enumerate(contours):
   area = cv2.contourArea(contour.astype(int))
   if (area>largest_area):
      largest_area=area
      largest_contour_index=i
LargestContour=contours[largest_contour_index]


def PlotContourAndSaveImage(height, width, channels,ImageBackGround,ContourImageLoc,cnt):
    fig, ax = plt.subplots(figsize=(width/100,height/100),frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.imshow(ImageBackGround, interpolation='nearest', cmap=plt.cm.gray,aspect='equal')
    ax.plot(cnt[:, 1], cnt[:, 0], linewidth=2)
    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(ContourImageLoc)
    plt.close()

#PlotContourAndSaveImage(height, width, channels,blackBackground,"C:/Users/Administrator/Desktop/JBM/blackedEdge2.JPG",LargestContour)


img = cv2.imread("C:/Users/Administrator/Desktop/JBM/blacked.JPG")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

contours = measure.find_contours(gray, 50,fully_connected='high', positive_orientation='high')














largest_area=0
for i,contour in enumerate(contours):
   area = cv2.contourArea(contour.astype(int))
   if (area>largest_area):
      largest_area=area
      largest_contour_index=i
LargestContour=contours[largest_contour_index]

fig, ax = plt.subplots()

def drawShape(img, coordinates, color):
    # In order to draw our line in red
    img = skimage.color.gray2rgb(img)

    # Make sure the coordinates are expressed as integers
    coordinates = coordinates.astype(int)

    img[coordinates[:, 0], coordinates[:, 1]] = color

    return img
for contour in contours:
    img = drawShape(img, contour, [255, 0, 0]) 


ax.imshow(img, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

