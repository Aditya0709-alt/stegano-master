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

    elif choice == "2":

