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