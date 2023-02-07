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

def remove(path):
    '''
    Method for removing the encoded file created.
    '''
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all it contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))

def split2len(s, n):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))




    

