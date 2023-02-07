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

def caesarAscii(char,mode,n):
    if mode == "enc" :
        ascii = ord(char)
        return chr((ascii + n) % 128)
    elif mode == "dec" :
        ascii = ord(char)
        return chr((ascii - n) % 128)


def encodeFrame(frameDir,textToHide,caesarn):
    textToHide_open = open(textToHide, "r")
    textToHide = repr(textToHide_open.read())

    # Split text to max 255 char each

    textToHide_chopped =  split2len(textToHide,255)

    for text in textToHide_chopped:
        length = len(text)
        chopped_text_index = textToHide_chopped.index(text)
        frame = Image.open(str(frameDir) +"/" + str(chopped_text_index+1) + ".png")

        if frame.mode != "RGB":
            print("Source frame must be in RGB format")
            return False

        # Use a copy of the file

        encoded = frame.copy()
        width, height = frame.size

        index = 0
        a = object
        for row in range(height):
            for col in range(width):
                r,g,b = frame.getpixel((col,row))

                # First value is length of the message per frame
                if row == 0 and col == 0 and index < length:
                    asc = length
                    if textToHide_chopped.index(text) == 0 :
                        total_encoded_frame = len(textToHide_chopped)
                    else:
                        total_encoded_frame = g
                elif index <= length:
                    c = text[index -1]
                    # put the encypted character into ascii value
                    asc = ord(caesarAscii(c,"enc",caesarn))
                    total_encoded_frame = g
                else:
                    asc = r
                    total_encoded_frame = g
                encoded.putpixel((col,row),(asc,total_encoded_frame,b))
                index += 1
        if encoded:
            encoded.save(str(frameDir)+"/"+str(chopped_text_index+1) + ".png",compress_level=0)


def decodeFrame(frameDir,caesarn):

    # Take the first frame to get width, height, and total encoded frame

    # first_frame = Image.open(str(frameDir) + "/0.jpg")
    first_frame = Image.open(str(frameDir)+ "/" + "1.png")
    r,g,b = first_frame.getpixel((0,0))
    total_encoded_frame = g
    msg = ""
    for i in range (1,total_encoded_frame+1):
        frame = Image.open(str(frameDir) + "/" + str(i) + ".png")
        width, height = frame.size
        index = 0
        for row in range(height):
            for col in range(width):
                try :
                    r,g,b = frame.getpixel((col,row))
                except ValueError:

                    # For some ong a(transparancy) is needed
                    r, g, b, a = frame.getpixel((col, row))
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    # Put the decrypted character into string
                    msg += caesarAscii(chr(r),"dec",caesarn)
                index +=1
    # Remove the first and the last quote
    msg = msg[1:-1]
    recovered_txt = open("data/recoveredText.txt", "w")
    recovered_txt.write(str(msg.encode().decode('unicode_escape')))

    

