# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:07:36 2024

@author: HP
"""

import numpy as np
import cv2
import math
from matplotlib import pyplot as plt
import argparse
import os
import glob


def writeimage(folder_name,filename,image):
    
    output_dir = os.path.join('G:/visual hel/', folder_name)


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, filename)

    cv2.imwrite(output_path, image)

def saveImages(file_name,img,k):
    k = str(k)
    writeimage(file_name[:-4]+'_laplacian', file_name[:-4]+'_laplacian'+'_k'+k+file_name[-4:], img)
    
def saveImages2(file_name,img,k):
    # k = str(k)
    writeimage('median_k15_2', file_name[:-4]+file_name[-4:], img)   
    
   


def laplacian():
    path = glob.glob('visual hel/test_images/*')
    c=0

    name=[]
    for file in path:
        print(file)
        file_name=os.path.basename(file).split('/')[-1]
        name.append(file_name)
        img = cv2.imread(file)
        # cv2.imshow("image",img)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for k in range(3,13,2):
            sharpen_img = cv2.Laplacian(gray_img, cv2.CV_64F, ksize=k)
            saveImages2(file_name,sharpen_img,k)
        
        # cv2.imshow("sharpened image",sharpen_img)
        c+=1
        if(c==1) :
            break
    # print(name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def laplacian2(k):
    path = glob.glob('visual hel/newz2/*')
    c=0

    name=[]
    for file in path:
        # print(file)
        file_name=os.path.basename(file).split('/')[-1]
        name.append(file_name)
    name = sorted(name, key=lambda x: int(os.path.splitext(x)[0]))
    # print(name[:20])
    n = len(name)
    for i in range(n):
       
        file = 'G:/visual hel/newz2/'+ name[i]
        # print(file)
        
          
        img = cv2.imread(file)
        # cv2.imshow("image",img)
        
        channels = cv2.split(img)
        
        if img is None:
            print(name[i])
            print(f"Warning: Could not read image {file}. Skipping...")
            continue

        # Split image into channels and check validity
        channels = cv2.split(img)
        if len(channels) == 0:
            print(name[i])
            print(f"Warning: Image {file} has no channels. Skipping...")
            continue
    #     # for k in range(3, 23, 2): 
            
        sharpened_channels = []
            
        for channel in channels:
                   
                        sharpened_channel = cv2.Laplacian(channel, cv2.CV_64F, ksize=k)
                        sharpened_channel = cv2.convertScaleAbs(sharpened_channel)  # Convert back to 8-bit
                        sharpened_channels.append(sharpened_channel)
        
                  
             
        sharpened_img = cv2.merge(sharpened_channels)
        sharpened_img = cv2.addWeighted(img, 1.5, sharpened_img, -0.5, 0)
        saveImages2(name[i],sharpened_img,k)
        
        # cv2.imshow("sharpened image",sharpened_img)
        c+=1
        print(c," ",name[i])
        # if(c==1) :
        #     break
    # print(name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
    
def median(k):
    path = glob.glob('G:/visual hel/newz2/*')
    c=0

    name=[]
    for file in path:
        # print(file)
        file_name=os.path.basename(file).split('/')[-1]
        name.append(file_name)
    name = sorted(name, key=lambda x: int(os.path.splitext(x)[0]))
    # print(name[:20])
    n = len(name)
    for i in range(n):
       
        file = 'visual hel/newz2/'+ name[i]
        # print(file)
        
          
        img = cv2.imread(file)
        # cv2.imshow("image",img)
        
        # channels = cv2.split(img)
        
        if img is None:
            print(name[i])
            print(f"Warning: Could not read image {file}. Skipping...")
            continue

      
        # for k in range(3, 23, 2): 
        blurred_img = cv2.medianBlur(img, k)
    
        # Sharpening by subtracting the blurred image from the original and adding it back
        sharpened_img = cv2.addWeighted(img, 1.5, blurred_img, -0.5, 0)
        saveImages2(name[i],sharpened_img,k)
        # cv2.imshow("sharpened image",sharpened_img)
        c+=1
        print(c," ",name[i])
        # if(c==1) :
        #     break
    # print(name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

# laplacian2(7)
median(15)































