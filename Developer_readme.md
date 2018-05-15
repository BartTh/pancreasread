
# Pancreasread
HTML5 and Javascript based webApp for automatic pancreas segmentation.

In order to run a virtual machine on the google cloud platform the following steps need to be followed:

1. Create a project with automatic billing to acquire GPU access
2. Navigate to compute engine
3. Create an instance with the following specs:
      - Zone: us-east1-d 
      - 1 vCPU
      - 4 GB RAM
      - 1 NVIDIA Tesla K80
      - Ubuntu 16.04 as boot disk
      - Allow HTTP & HTTPS traffic
      - Set a static external IP-address
      - Settings which are not mentioned can be left to default

Note: other zones are possible for usage of Tesla P100 GPUs, however us zones do no require deposit of own funds.

4. Navigate to  https://developer.nvidia.com/cuda-downloads and install CUDA 8.0:
      > sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb\
      sudo apt-get update\
      sudo apt-get install cuda
5. Verifiy proper installation of the drivers by running:
	> nvidia-smi

6. NVIDIA provides the cuDNN library to optimize neural network calculations on their cards, this enhances performance and can be acquired by: 
	> 	cd $HOME \
	tar xzvf libcudnn6_6.0.21-1+cuda8.0_amd64.deb \
	sudo cp cuda/lib64/* /usr/local/cuda/lib64/  \
	sudo cp cuda/include/cudnn.h /usr/local/cuda/include/ \

7. Install packages and tensorflow 1.4
	> sudo apt-get install python-dev python3-pip libcupti-dev \

8. Install other libraries necessary 
	> pip3 install click \ 
	pip3 install numpy \  
	pip3 install SimpleITK  \
	pip3 install scikit-image \ 
	pip3 install toolz  \
	pip3 install sklearn \  
	pip3 install tensorflow-gpu==1.4

9. Copy folder `HULK/HJHUISMAN/pancreasread` from the hulk disk
