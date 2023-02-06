from pyfiglet import Figlet
#print(pyfiglet.FigletFont.getFonts())


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
        file_name = input("Enter the name of the video file in the folder: ")

        try:
            caesarn = int(input("Enter Caesar cypher value: "))
        except ValueError:
            print("")
            print("The value is not an integer ")
            exit()

        try:
            open("data/" + file_name)
        except IOError:
            print("")
            print("File not found")
            exit()



