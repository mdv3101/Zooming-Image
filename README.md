*Take any image as input and give a zoomed image as output.

*Use pivot point (where to zoom) and scale as parameters.

*Width and height needs to be same of input and output image.

Notes

*Use the snippet code provided above as a starting point. DO NOT import any additional libraries/packages. Do not use NumPy functions/methods in your code.

*Use image libraries for loading and saving images only. Do not use it for implementing zooming.

*Pivot point should be at the center in the output image, make sure you handle all the corner cases. i.e at cases where the image size can not be the same as input size handle accordingly with the pivot point. For example, if the pivot point is the top-left corner then the location of pivot point in the output image is at top-left or if it is at center of the bottom edge, then it’s in the output image is at bottom-center and likewise.

*Your implementation should avoid artifacts as much as possible.

*Bonus points if you implement K-Times Zooming algorithm.

