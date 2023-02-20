from pyfiglet import Figlet
from helpers import *
from subprocess import call,STDOUT
import os

if __name__ == '__main__':

    f = Figlet(font='slant')
    print(f.renderText("CCVS"))
    print("CaesarCipherVideoSteganography")
    print("")

    print("Menu :")
    print("")
    print("a. Encypt & Merge into Video")
    print("b. Decrypt & Get the plain text")
    print("-----------------------")
    choice = input("(!) Choose option : ")

def encrypt():
    call(["clear"])

        print(f.renderText("Encrypt"))
        print("----------------------------------------")
        file_name = input("Enter the video file name in the data folder: ")

        try:
            caesarn = int(input("Caesar cypher value: "))
        except ValueError:
            print("-----------------------")
            print("The value is not an integer ")
            exit()

        try:
            open("data/" + file_name)
        except IOError:
            print("-----------------------")
            print("File not found ")
            exit()

        print("-----------------------")
        print("Extracting Frame(s)")
        frame_extract(str(file_name))
        print("Extracting audio")

        call(["ffmpeg", "-i", "data/" + str(file_name), "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

        print("(-) Reading text-to-hide.txt")
        print("(-) Encrypting & appending string into frame(s) ")
        encode_frame("temp", "data/text-to-hide.txt", caesarn)
        print("(-) Merging frame(s) ")

        call(["ffmpeg", "-i", "temp/%d.png" , "-vcodec", "png", "temp/video.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

        print("(-) Optimizing encode & Merging audio ")

        call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy","data/enc-" + str(file_name)+".mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        print("(!) Success , output : enc-" + str(file_name)+".mov")
 
def decrypt():
    call(["clear"])

        print(f.renderText("Decrypt"))
        print("----------------------------------------")
        file_name = input("Enter the video file name in the data folder: ")

        try:
            caesarn = int(input("Caesar cypher value: "))
        except ValueError:
            print("-----------------------")
            print("The value is not an integer ")
            exit()

        try:
            open("data/" + file_name)
        except IOError:
            print("-----------------------")
            print("File not found ")
            exit()

        print("-----------------------")
        print("Extracting Frame(s)")
        frame_extract(str(file_name))
        print("Decrypting Frame(s)")
        decode_frame("temp",caesarn)
        print("Writing to recovered-text.txt")
        print("Success")


   
