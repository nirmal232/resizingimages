import cv2
img= cv2.imread("E:/img/spiderman.jpg",cv2.IMREAD_UNCHANGED)
print('Original Dimensions:',img.shape)
'''
The folder structure may vary from individual machines , please 
replace the write and read path accordingly
'''

#Downscaling
scale_percent = 60 # percent of original size 
width = int(img.shape[1] * scale_percent / 100) 
height = int(img.shape[0] * scale_percent / 100) 
dim = (width, height) 
# resize image in down scale 
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions : ',resized.shape) 
cv2.imwrite('E:/img/resize.jpg', resized)


#upscaling

scale_percent = 220 # percent of original size 
width = int(img.shape[1] * scale_percent / 100) 
height = int(img.shape[0] * scale_percent / 100) 
dim = (width, height) 
# resize image in up scale 
resized_up = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions : ',resized_up.shape) 
cv2.imwrite('E:/img/resize_upscale.jpg', resized_up)

#resize only width
width = 440 
height = img.shape[0] # keep original height 
dim = (width, height) 
# resize image 
resized_w = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions : ',resized_w.shape) 
cv2.imwrite('E:/img/resize_width.jpg', resized_w) 

#resize only height
width = img.shape[1] # keep original width 
height = 440 
dim = (width, height)
 # resize image 
resized_h = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions : ',resized_h.shape) 
cv2.imwrite('E:/img/resize_height.jpg', resized_h)

#resize width and height
width = 350 
height = 450 
dim = (width, height) 
# resize image 
resized_hw = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions : ',resized_hw.shape) 
cv2.imwrite('E:/img/resize_hw.jpg', resized_hw) 

cv2.waitKey(0)
cv2.destroyAllWindows()
