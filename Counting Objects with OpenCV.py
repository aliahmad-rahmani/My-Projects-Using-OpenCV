
# import libraries
import numpy as np
import cv2


# load image
img = cv2.imread('2.png')
# Determine the shape of image
print(img.shape)


# prepare image : blur and convert to grey scale, another way is to use img = cv2.imread('2.png',0)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (17, 17), 0)

# show blurred image and grey scaled image and save images
cv2.imshow('grey scale', grey)
cv2.imwrite('grey scale.png',grey)
cv2.imshow('blurred', blurred)
cv2.imwrite('blurred.png',blurred)
"""
# canny edge detector the key point is use of apertureSize = 5 the defult one is 3 and its the kernel of sobel filter in canny 
you can try by delete it and you will see some coins wont detect
"""
outline = cv2.Canny(blurred, 30,150,apertureSize = 5)

# show canny edge detector and save image
cv2.imshow('The edges', outline)
cv2.imwrite('The edges.png',outline)



# find the contours and so the number of coins
(cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('I found %i coins' % len(cnts))


# draw contours: -1 will draw all contours and (0, 255, 0) is green color and 2 is Thickness of line then show result and finally save it
cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
cv2.imshow('Result', img)
cv2.imwrite('Result.png',img)

#Determine the coordinates of circle's centers or coin's center
for (i, c) in enumerate(cnts):
     ((x, y), _) = cv2.minEnclosingCircle(c)
     print(12-i,' : ',int(x),'   ',int(y))
     print('******')
     #cv2.putText(img, "{}".format(12-i), (int(x) , int(y)+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2 )
"""
this loop dont work appropriately for number the coins (you can try! just put off "#" of line 56 and you will see!)
but we can use the coordinates of center of each coins
"""

#store the coordinates in arry in range and then put number for each center of coin in range
arr=np.array([[[61,66],[175,109],[305,72],[440,110]],[[78,200],[192,233],[313,202],[414,230]],[[96,309],[180,337],[316,308],[412,332]]])
a=1 #flag to count coins
for i in range(3):
  for j in range(4):
      cv2.putText(img,"{}".format(a),(arr[i][j][0],arr[i][j][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
      a+=1
      

# show final_Result and save it
cv2.imshow('final_Result', img)
cv2.imwrite('final_Result.png',img)

#for see all image and it cause to not close these images
cv2.waitKey()
cv2.destroyAllWindows()

