# Stegano-Master

![stegano-master](https://user-images.githubusercontent.com/77115883/219879947-d524012a-63b5-47ee-9632-daad2e168e39.jpeg)


*The art of hiding important information with ordinary information to avoid detection!*

# Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [About the package](#about-the-package)
  - [Features](#features)
  - [Dependencies](#dependencies)
  - [Initial setup](#initial-setup)
  - [Creating releases](#creating-releases)
- [Contributors](#contributors)


# Introduction

Steganography is the art of hiding the fact that communication is taking place, by hiding information in other information. Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. 

In video steganography we have used combination of cryptography and Steganography. We encode the message through two parts:-

- We convert plaintext to cipher text for doing so we have used Caeser-Cipher Encryption Algorithm. t is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
- For encryption, the video will be converted into raw .mov video to make sure data in the video won't change after re-encoding and decryption, and make sure you got enough space
- A temp folder will be created to dump temporary extracted frame , audio, and video data.

To view our demonstration : https://www.youtube.com/watch?v=QhhfpK6KFrU

# Architecture

![Screenshot 2023-02-18 at 11 29 00 PM](https://user-images.githubusercontent.com/77115883/219881271-e892fc18-7b9b-4b9c-9186-81949a7ba31a.jpg)


# About the package

- Making this project into a PyPi package was the first step to make the project public.
- We created a package 'stegano-master' which can be installed directly using pip and integrated with any project out there.
- Check out our published package on PyPi here : https://pypi.org/project/stegano-master/0.0.1/

## Features

- Frame extraction and merging 
- Audio to text conversion
- Video encryption and decryption
- Reading text and appending to frame


## Dependencies
![image](https://user-images.githubusercontent.com/77115883/219881788-0f04f271-5e66-4e09-90ce-2395a50c4d7f.png)

```python3
ffmpeg
Pillow
opencv-python
pyfiglet
```

## Initial Setup

Install the package using the command:

```python3
pip install stegano-master
```

Then, import the different methods as:

```python3
from stegano-master.main import encrypt, decrypt

#For encryption
encrypt()

#For decryption
decrypt()

```

## Creating-releases

For streamlining the continuous integration and depolyment of your application, you can also Dockerize the app. 

- Create a Dockerfile and add the following to it:

```docker
FROM python:3.9
WORKDIR /app

# Install regular packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install submodule packages
COPY _submodules/stegano-master _submodules/stegano-master
RUN pip install _submodules/stegano-master--upgrade

# copy source code
COPY ./ .

# command to run on container start
CMD [ "python", "./main.py"]
```

- Run the following commands

```docker
docker build -t my_image --rm .

docker run -it --name stegano-master --rm my_image

```
- This will create a Docker container on your local machine. 

![Screenshot 2023-02-19 at 8 50 54 PM](https://user-images.githubusercontent.com/77115883/219957525-6855e7d0-08b7-4e55-ab3a-d600c040cc06.jpg)

- Then, you can run the CLI app inside your container.

![Screenshot 2023-02-19 at 8 56 04 PM](https://user-images.githubusercontent.com/77115883/219957705-f6546ea8-06fc-4d40-9465-d80dad32518a.jpg)

- Whatever changes you make to the package will be updated continuously.


# Contributors

| Name               | Profile |
| -------------------| ----------------|
| Aditya Pawar       | [Aditya0709-alt](https://github.com/Aditya0709-alt)  |
| Ujjwal Kumar       | [Ukd1796](https://github.com/Ukd1796)        |
| Shruti Tyagi       | [shrutityagi4102](https://github.com/shrutityagi4102) |
