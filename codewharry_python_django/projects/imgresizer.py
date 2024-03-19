import cv2

source="bachira.jpg"
destination='newimg.png'
scale_percent = 50


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

newwidth = int(src.shape[1] * scale_percent / 100)
newheight = int(src.shape[0] * scale_percent / 100)


output = cv2.resize(src, newwidth, newheight)

cv2.imwrite(destination,output) 

cv2.waitKey (0)