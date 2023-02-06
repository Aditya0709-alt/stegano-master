from PIL import Image
import os 
import cv2
import shutil


def extractFrame(video):
    '''
    Method to extract frames(images) from the video using VideoCapture.
    '''
    tempFolder = 'temp'
    try:
        os.mkdir(
            
        )