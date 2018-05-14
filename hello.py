#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import flask
import glob
import gzip
import numpy as np
import nibabel
import os
import SimpleITK as sitk
import sys

sys.path.append('/home/bartrthomson/igor2')
from flask import Flask, render_template, request
from igor2.core import load_nii, save_json
from scipy import ndimage
from shutil import copy2
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/'
EXTENSION = '*.nii'
ALLOWED_EXTENSIONS = set(['gz'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def list_files1(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith(tuple(extension)))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def create_json(num):
    os.chdir('/tmp/')

    metadata = {'scans': {},
                'cumed-build-tfrecords': {
            "augment_probability": 0.25,
            "channels": [
                "CT"
            ],
            "input_shape": [
                16,
                64,
                64,
                1
            ],
            "num_classes": 2,
            "num_instances": 1000,
            "random_seed": 0
        }}
    scandict = {}
    scandict1 = {'validation': {}}

    segment = load_nii('/tmp/{}'.format(num))
    segment = segment.astype(bool).astype(np.uint8)
    segment = np.flipud(segment)

    assert np.unique(segment).tolist() == [0, 1], (num, np.unique(segment))
    np.save('/tmp/SCAN.npy', segment)
    scandict['CT'] = '/tmp/SCAN.npy'
    scandict1['validation']['SCAN'] = scandict
    metadata['scans'] = scandict1

    save_json('test.json', metadata)

def first_file(folder):
    list_of_files = glob.glob(folder)
    try:
        output = max(list_of_files, key=os.path.getctime)
    except ValueError:
        output = 'Empty!'

    create_json(output[5:])

    return output

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            copy2('/tmp/' + filename, '/home/bartrthomson/flask_app/static/Pancreas_PANCREAS_0057.nii')
            copy2('/tmp/' + filename, '/home/bartrthomson/flask_app/static/Uploaded_Scan.nii')

            for src_name in glob.glob(os.path.join(UPLOAD_FOLDER, filename)):
                base = os.path.basename(src_name)
                dest_name = os.path.join(UPLOAD_FOLDER, base[:-3])
                with gzip.open(src_name, 'rb') as infile:
                    with open(dest_name, 'wb') as outfile:
                        for line in infile:
                            outfile.write(line)

    return render_template('index.html')

@app.route("/stream")
def stream():
    from shelljob import proc
    first_file(UPLOAD_FOLDER + EXTENSION)
    g = proc.Group()
    bashCommand = "python3 /home/bartrthomson/igor2/bin/cumed-predict /tmp/test.json /home/bartrthomson/results/antwoord/fold-01/checkpoints/cumed-56000 /tmp/"
    sys.path.append('/home/bartrthomson/igor2/bin')
    p = g.run( [ "bash", "-c", bashCommand ] )
    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield line
                term = b'Done. Terminating...'

                if term in line: #see if one of the words in the sentence is the word we want
                    output = '/tmp/SCAN-segmentation.npy'
                    print('SEGMENTED FILE LOCATION::: ' + output)
                    data = np.load(output)
                    data = data[:, ..., 1]
                    data = np.rot90(data, 3, axes=(0, 2))
                    data = np.flipud(data)
                    data = data > 0.2

                    # Generate binary structure for biggest 3D region selection
                    s = ndimage.generate_binary_structure(3, 3)  # iterate structure
                    labeled_array, numpatches = ndimage.label(data, s)  # labeling

                    sizes = ndimage.sum(data, labeled_array, range(1, numpatches + 1))
                    # To get the indices of all the min/max patches. Is this the correct label id?
                    map = np.where(sizes == sizes.max())[0] + 1

                    # Inside the largest, respecitively the smallest labeled patches with values
                    max_index = np.zeros(numpatches + 1, np.uint8)
                    max_index[map] = 1
                    data = max_index[labeled_array]                 # Biggest region

                    np.save('/tmp/temp.npy', data)
                    data = data.astype(float)
                    data = nibabel.Nifti1Image(data, affine=np.eye(4))
                    nibabel.save(data, "/tmp/SCAN-segmentation.nii")
                    segmentation_out = sitk.ReadImage(r'/tmp/SCAN-segmentation.nii')
                    sitk.WriteImage(segmentation_out, r'/home/bartrthomson/flask_app/static/SCAN-segmentation.nii.gz')

                    yield 'RETURN TO MAIN PAGE AND PRESS ANALYZE'

    return flask.Response(read_process(), mimetype= 'html')

@app.route("/view")
def view():
    data = np.load('/tmp/temp.npy')
    output = np.sum(data)/1000

    return render_template('viewer.html', output = output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
