

#This line imports the OpenCV library, which is used for computer vision and image processing tasks
import cv2 


#It reads an image file named 'image_to_sketch\lisa.jpg' from the directory and stores it in the image1 variable. This image is considered the input image.
laliimage = cv2.imread('image_to_sketch\lisa.jpg')

window_name = 'Actual image'   #Defines a window name to display the original image
cv2.imshow(window_name, laliimage) #Displays the original image in a window with the specified window name using OpenCV's imshow function.

#Converts the original color image (image1) to grayscale using the cvtColor function. Grayscale images have only one channel representing pixel intensity.
grey_img = cv2.cvtColor(laliimage, cv2.COLOR_BGR2GRAY) 


#Inverts the grayscale image using bitwise_not operation. This results in a negative-like effect.
invert = cv2.bitwise_not(grey_img)

#Applies Gaussian blur to the inverted image to smooth it out. 
#This helps in reducing noise and creating a smoother sketch-like appearance.
blur = cv2.GaussianBlur(invert, (21, 21), 0)  
invertedblur = cv2.bitwise_not(blur)  #Inverts the blurred image back to obtain a positive-like effect.

#Divides the grayscale image by the inverted blurred image. This division operation enhances the edges and features, creating a sketch effect. The scale parameter is used to adjust the contrast.
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)


def divide(grey_img, b, invertedblur=256.0):
    return (grey_img * scale) / invertedblur


cv2.imwrite("sketch.jpeg", sketch)
image = cv2.imread("sketch.jpeg") # It reads an image file named 'lisa.jpg' from the 'sketch' directory and stores it in the image1 variable. This image is considered the input image.
window_name ='Sketch image'
cv2.imshow(window_name, image)

#Waits for a keyboard event indefinitely, allowing you to view the original and sketch images in the displayed windows until a key is pressed.
cv2.waitKey(0)


