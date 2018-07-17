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


img = np.asarray(image)
l,b,h =img.shape

aa = np.zeros((scale*(l-1)+1,scale*(b-1)+1,h))
aa1 = np.zeros((scale*(l-1)+1,scale*(b-1)+1,h))

##K-Times Zooming Algorithm
#row wise
j1=0

for i in range (0,l):
    for j in range(0,b-1):
        for k in range (0,h):
            if (img[i][j][k] <= img[i][j+1][k]):
                op = img[i][j+1][k] - img[i][j][k]
                op = op/scale
                for n in range(0,scale):
                    aa[i][j1+n][k] = img[i][j][k]+(op*n)
            else:
                op = img[i][j][k] - img[i][j+1][k]
                op = op/scale
                for n in range(0,scale):
                    aa[i][j1+n][k] = img[i][j][k]-(op*n) #To avoid sorting, subtract the value of OP from larger value and store it diectly.
        j1 = j1+scale
    aa[i][j1][:] = img[i][j+1][:]
    j1=0
    

#column wise

i1=0

for j in range (0,scale*(b-1)+1):
    for i in range(0,l-1):
        for k in range (0,h):
            if (aa[i][j][k] <= aa[i+1][j][k]):
                op = aa[i+1][j][k] - aa[i][j][k]
                op = op/scale
                for n in range(0,scale):
                    aa1[i1+n][j][k] = aa[i][j][k]+(op*n)
            else:
                op = aa[i][j][k] - aa[i+1][j][k]
                op = op/scale
                for n in range(0,scale):
                    aa1[i1+n][j][k] = aa[i][j][k]-(op*n) #To avoid sorting, subtract the value of OP from larger value and store it diectly.
        i1 = i1+scale
    aa1[i1][j][:] = aa[i+1][j][:]
    i1=0

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


zoomed_image = aa1[x1:x2,y1:y2]
cv2.imwrite("zoomed_image.png", np.array(zoomed_image, dtype="uint8"))
