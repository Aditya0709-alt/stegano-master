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
        os.mkdir(tempFolder)
    except OSError:
        remove(tempFolder)
        os.mkdir(tempFolder)
    
    vidcap = cv2.VideoCapture("data/" + str(video))
    count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(tempFolder, f"{count}.png"), image)
        count += 1

    

