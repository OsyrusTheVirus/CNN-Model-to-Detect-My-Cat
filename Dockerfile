# Dockerfile so that I don't have to manually install everything.

FROM python

# linux package manager
RUN apt-get update

# python package manager and updating it
RUN pip install --upgrade pip
RUN pip --version

# installing make to use the make file
RUN apt-get -y install make

# pytorch cpu version only (I'm not using a GPU, so I'm ignoring GPU libraries)
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Bash shell
CMD ["bash"]