# pancreasread
WebApp for pancreas segmentation

In order to run a virtual machine on the google cloud platform the following steps need to be followed:

1. Create a project
1. Navigate to compute engine
1. Create an instance with the following specs:
      - 1 vCPU
      - 4 GB RAM
      - 1 NVIDIA Tesla K80
      - Ubuntu 16.04 as boot disk
      - Allow HTTP & HTTPS traffic
      - Set a static external IP-address
      - Settings which are not mentioned can be left to default
1. Install CUDA 8.0:
      > sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
      > sudo apt-get update
      > sudo apt-get install cuda


