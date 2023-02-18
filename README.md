# Stegano-Master

![stegano-master](https://user-images.githubusercontent.com/77115883/219879947-d524012a-63b5-47ee-9632-daad2e168e39.jpeg)


*The art of hiding the important information with the ordinary information to avoid detection!*

# Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- About the package(#package)
  - Features(#features)
  - [Initial setup](#initial-setup)
  - [Creating releases](#creating-releases)
- [FAQ](#faq)
- [Contributing](#contributing)


# Introduction

Steganography is the art of hiding the fact that communication is taking place, by hiding information in other information. Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. 

In video steganography we have used combination of cryptography and Steganography. We encode the message through two parts:-

- We convert plaintext to cipher text for doing so we have used Caeser-Cipher Encryption Algorithm. t is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
- For encryption, the video will be converted into raw .mov video to make sure data in the video won't change after re-encoding and decryption, and make sure you got enough space
- A temp folder will be created to dump temporary extracted frame , audio, and video.

# Architecture

![Screenshot 2023-02-18 at 11 29 00 PM](https://user-images.githubusercontent.com/77115883/219881271-e892fc18-7b9b-4b9c-9186-81949a7ba31a.jpg)


