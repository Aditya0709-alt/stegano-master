# Stegano-Master

![stegano-master](https://user-images.githubusercontent.com/77115883/219879947-d524012a-63b5-47ee-9632-daad2e168e39.jpeg)


*The art of hiding important information with ordinary information to avoid detection!*

# Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [About the package](#package)
  - [Features](#features)
  - [Dependencies](#dependencies)
  - [Initial setup](#initial-setup)
  - [Creating releases](#creating-releases)
- [FAQ](#faq)
- [Contributors](#contributors)


# Introduction

Steganography is the art of hiding the fact that communication is taking place, by hiding information in other information. Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. 

In video steganography we have used combination of cryptography and Steganography. We encode the message through two parts:-

- We convert plaintext to cipher text for doing so we have used Caeser-Cipher Encryption Algorithm. t is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
- For encryption, the video will be converted into raw .mov video to make sure data in the video won't change after re-encoding and decryption, and make sure you got enough space
- A temp folder will be created to dump temporary extracted frame , audio, and video.

# Architecture

![Screenshot 2023-02-18 at 11 29 00 PM](https://user-images.githubusercontent.com/77115883/219881271-e892fc18-7b9b-4b9c-9186-81949a7ba31a.jpg)


# About the package

- Making this project into a PyPi package was the first step to make the project public.
- We created a package 'stegano-master' which can be installed directly using pip and integrated with any project out there.

# Features

- Frame extraction and merging 
- Audio to text conversion
- Video encryption and decryption
- Reading text and appending to frame


# Dependencies
![image](https://user-images.githubusercontent.com/77115883/219881788-0f04f271-5e66-4e09-90ce-2395a50c4d7f.png)

```python3
ffmpeg
Pillow
opencv-python
pyfiglet
```

# Initial Setup

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


# Contributors

| Name               | GitHub Username |
| -------------------| ----------------|
| Aditya Pawar       | [Aditya0709-alt](https://github.com/Aditya0709-alt))  |
| Ujjwal Kumar       | [Ukd1796](https://github.com/Ukd1796)        |
| Shruti Tyagi       | [shrutityagi4102](https://github.com/shrutityagi4102) |
