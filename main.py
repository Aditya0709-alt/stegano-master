from pyfiglet import Figlet
#print(pyfiglet.FigletFont.getFonts())
from helpers import extractFrame
from subprocess import call, STDOUT
import os


if __name__ == "__main__":
    fig = Figlet(font="computer")
    print(fig.renderText("Video Steganography"))


    print("Welcome")
    print("")
    print("Enter 1 for Encrypt and merge into the video")
    print("Enter 2 for Decrypt and get the plain text")
    print("")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(fig.renderText("Encrypt.."))
        print("")
        fileName = input("Enter the name of the video file in the folder: ")

        try:
            caesarn = int(input("Enter Caesar cypher value: "))
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
        The library is installed globally and we make system calls to the 
        '''

        call(["ffmpeg", "-i", "data/" + str(fileName), "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        
        print("Reading the text needed to be hidden")
        print("Encrypting & appending string into frames")
        




