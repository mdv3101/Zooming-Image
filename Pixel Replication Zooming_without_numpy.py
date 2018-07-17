import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to input image", required=True)
ap.add_argument("-p", "--pivot-point", help="Pivot point coordinates x, y separated by comma (,)", required=True)
ap.add_argument("-s", "--scale", help="Scale to zoom", type=int, required=True)
args = vars(ap.parse_args())

image_path = args["image"]
x, y = map(int, args["pivot_point"].split(","))
scale = args["scale"]
image = cv2.imread(image_path)
image = image.tolist()

"""
WRITE YOUR CODE HERE

"""
def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])

dimm = dim(image)
l,b = dimm[0], dimm[1]
channel = dimm[2]


#row wise
ab=[]
ab2=[]
for row in image:
    for ro in row:
        for i in range(0,scale):
            ab.append(ro)
    ab2.append(ab)
    ab=[]

#column wise
rlist=[]
for a in ab2:
    for i in range(0,scale):
        rlist.append(a)

x1 = int((x*scale) - l/2)
x2 = int((x*scale) + l/2)
y1 = int((y*scale) - b/2)
y2 = int((y*scale) + b/2)

if (x1<0):
    x2 = x2-x1
    x1=0
if (x2>(l*scale)):
    x1 = x1 - (x2-(l*scale))
    x2 = l*scale


if (y1<0):
    y2 = y2-y1
    y1=0

if (y2>(b*scale)):
    y1 = y1 - (y2-(b*scale))
    y2 = b*scale

zoomed_image = []
for i in range(x1,x2):
    zoomed_image.append(rlist[i][y1:y2])
cv2.imwrite("zoomed_image.png", np.array(zoomed_image, dtype="uint8"))
