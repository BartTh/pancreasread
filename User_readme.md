
# Pancreasread
HTML5 and Javascript based webApp for automatic pancreas volume segmentation.

In order to use the pancreatic analysis tool there are certain steps to be followed:

1. Login to the [google cloud platform](https://console.cloud.google.com/compute/) with the pancreasread account
2. Start the instance by clicking on the three vertical dots to the far right of th einstance name
3. Wait for the virtual machine to be ready
4. Connect to the virtual machine by clicking SSH
5. When the command line interface appears (linux) type the following:
  > screen
  - press spacebar to clear the screen help
  > cd flask_app
  > gunicorn -t 400 hello:app
6. Navigate to the external IP address by clicking the address left of SSH mentioned in step 4
7. Upload a scan that has been converted to the .nii.gz format
