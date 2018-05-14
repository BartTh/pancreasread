Pancreasread user manual
=====

The user manual consists of two parts, acquiring access to the virtual machine, and converting a scan to the `.nii.gz` format

Connect to the virtual machine (VM)
-----

In order to use the pancreatic analysis tool there are certain steps to be followed:

1. Login to the [google cloud platform](https://console.cloud.google.com/compute/) with the pancreasread account
1. Start the instance by clicking on the three vertical dots to the far right of the instance name
1. Wait for the virtual machine to be ready
1. Connect to the virtual machine by clicking `SSH`
1. When the command line interface appears (linux) type the following:
  > screen
6. Press spacebar to clear the screen help and type:
  > cd flask_app;
  > gunicorn -t 400 hello:app
7. Close the command line interface, confirm exit when prompt appears
8. Navigate to the external IP address by clicking `external address` left of SSH mentioned in step 4
9. Upload a scan that has been converted to the .nii.gz format
10. When the upload is finished, press `Continue` to continue
11. Go back to the main page when the last line reads 'RETURN TO MAIN PAGE AND PRESS VIEW'
12. Press 'view' to view the segmentation visualization and volume estimation (cm^3)
13. Adjust settings to preference
14. Stop the instance by clicking on the three vertical dots to the far right of the instance name when finished

Convert the scans to .nii.gz
-----
