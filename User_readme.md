Pancreasread user manual
=====

The user manual consists of two parts, acquiring access to the virtual machine, and converting a scan to the `.nii.gz` format

Connect to the virtual machine (VM)
-----

In order to use the pancreatic analysis tool there are certain steps to be followed:

1. Use Google Chrome to continue the following steps
1. Login to the [google cloud platform](https://console.cloud.google.com/compute/) with the pancreasanalyse account
1. Start the instance by clicking on the three vertical dots to the far right of the instance name
1. Click the option `Begin` from the drop down menu that appears
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

Scans generated in the clinic are saved as DICOM files and contain personal patient data. This data can be stripped by converting it to the NifTi file format (.nii), resulting in just the pixel values with some data about spacial orientation. In order to enhance processing speed and data transfer, the files can be compressed to the gzip (.gz). A way to convert and compress simultaneously is by using the Matlab script developed by [Xiangrui Li](https://nl.mathworks.com/matlabcentral/fileexchange/42997-dicom-to-nifti-converter--nifti-tool-and-viewer). It is used in the following manner:

1. [Download](https://nl.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/42997/versions/92/download/zip) the Matlab DICOM to NifTi converter
1. Extract the file `dicm2nii.m` to a folder of choice and open it with Matlab
1. Run the file by pressing `F5`, when prompted click `Add to Path`
1. Browse the folder or files by means of the DICOM to NifTi converter that popped up
1. Determine the output folder by pressing `Result folder`
1. Select `.nii` as output format and tick `Compress` and `SPM 3D`
1. In the preferences box tick the following: `Left-hand storage` and `Use parfor if needed`
1. When the form is filled out, press `Start conversion`
1. These files can then be uploaded to the static IP adress described in step 8. under connecting to the virtual machine
