from pyfiglet import Figlet, FigletFont
#print(FigletFont.getFonts())
from helpers import extractFrame, encodeFrame, decodeFrame
from subprocess import call, STDOUT
import os
from server import *


fig = Figlet(font="shadow")
print(fig.renderText("Video Steganography"))


# print("Welcome")
# print("")

# print("Enter whether to encrypt or decrypt")
# print("")
# choice = input("Enter your choice: ")



def encrypt():
    print(fig.renderText("Encrypt.."))
    print("")
    fileName = "chef.mp4"

    try:
        caesarn = 5
    except ValueError:
        print("")
        print("The value is not an integer ")
        exit()

    try:
        open("data/" + fileName)
    except IOError:
        print("")
        print("File not found")
        exit()

    print('')
    print("Extracting frames")
    extractFrame(str(fileName))
    print("Extracting audio")

    '''
    For converting the mp4 file to audio i.e. mp3, we use a library called ffmpeg.
    The library is installed globally and we make system calls.
    '''

    call(["ffmpeg", "-i", "data/" + str(fileName), "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        
    print("Reading the text needed to be hidden")
    print("Encrypting & appending string into frames")
    encodeFrame("temp", "data/textToHide.txt", caesarn)
    print("Merging frames")
    #ffmpeg -i temp/%d.png -vcodec png data/enc-filename.mov
    call(["ffmpeg", "-i", "temp/%d.png" , "-vcodec", "png", "temp/video.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

    print("Optimizing encode & Merging audio ")
    # ffmpeg -i temp/temp-video.avi -i temp/audio.mp3 -codec copy data/enc-chef.mp4 -y
    call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy","data/enc-" + str(fileName)+".mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    print("Success , output : enc-" + str(fileName)+".mov")

def decrypt():
        # refresh terminal
        call(["clear"])

        print(fig.renderText("Decrypt"))
        print("----------------------------------------")
        fileName = input("Video file name in the data folder: ")

        try:
            caesarn = int(input("Caesar cypher value: "))
        except ValueError:
                
            print("(!) n is not an integer ")
            exit()

        try:
            open("data/" + fileName)
        except IOError:
                
            print("(!) File not found ")
            exit()

            
        print("Extracting Frames")
        extractFrame(str(fileName))
        print("Decrypting Frames")
        decodeFrame("temp",caesarn)
         #useless
        print("Writing to recoveredText.txt")
        print("(!) Success")









            




