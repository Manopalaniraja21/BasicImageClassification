import sys

import matplotlib.pyplot as plt
import os
import numpy as np
import easygui
import cv2


def upload():
    image_path = easygui.fileopenbox();
    return image_path


def cartoonify(image_path):
    originalImage = cv2.imread(image_path)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    if originalImage is None:
        print("No image found ,choose some other file")
        sys.exit()
    # Resized image
    resizedImage = cv2.resize(originalImage, (960, 540))
    # Gray scale image
    grayscaleimage=cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)
    resizedImageGray=cv2.resize(grayscaleimage,(960,540))
    # Blurred gray scale image for smoothening the image
    smoothenBlurGray=cv2.medianBlur(resizedImageGray,5)
    resizedImageGrayBlurred=cv2.resize(smoothenBlurGray,(960,540))
    # Creating the outline of the image by retrieving the edge
    # Using the thresh-hold technique
    getEdge=cv2.adaptiveThreshold(resizedImageGrayBlurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    resizedImageEdge=cv2.resize(getEdge,(960,540))
    # Prepare the mask image
    # Applying bilateral image to remove the noise
    # And keep edge is sharped
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    resizedImageColor = cv2.resize(colorImage, (960, 540))
    # Cartoon image
    # Masking edge image with Beautify Image

    cartoonImage=cv2.bitwise_and(resizedImageColor,resizedImageColor,mask=resizedImageEdge)

    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    # plt.imshow(resizedImage,cmap='gray')
    # plt.imshow(resizedImageGray,cmap='gray')
    # plt.imshow(smoothenBlurGray,cmap='gray')
    # plt.imshow(resizedImageEdge,cmap='gray')
    plt.imshow(cartoonImage)
    plt.show()

x=upload()
cartoonify(image_path=x)
sys.exit()





