from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A package for hiding text within videos and sending the encrypted videos'
LONG_DESCRIPTION = 'A simple program written in python to hide encrypted text using simple caesar cipher in video frames, the encryption algorithm could be easily changed because the cipher algorithm is loosly coupled'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="stegano-master", 
        version=VERSION,
        author="Aditya Pawar",
        author_email="<aditya.pawar2@somaiya.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['rfc3986','rich','six','urllib3','webencodings','zipp','Pillow','pyfiglet'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)