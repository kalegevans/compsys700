# COMPSYS700: Introdution
This is project #97 of the 2018 University of Auckland ECE Part IV projects. The intent of this research is
to provide an automated emergency callout system for heart disease patients in life threatening events. 

Our repository contains:
1. `/signalprocessing', contains wfdb and MATLAB code to preprocess Physionet datasets. This involves the detection of R-R intervals using a QRS detection algorithm, finding and correcting ectopic beats, and filling with averages. Time domain, frequency domain and non-linear metircs were output. The correction step was necessary to avoid garbage frequency domain values, which is highly sensitive to noise artifacts/random spikes. Two datasets used: nsrdb, cudb - normal sinus rhythm database, Creighton University Ventricular Tachyarrhythmia Database
2. `/machinelearning', code to work the back propogation neural network. 3 inputs proposed (LF, HF, LF/HF), 2 outputs (NSR or VT/VF). One middle layer with 15 neurons, using gradient descent with cost functions to learn.
3. `/apps`, code regarding the interim PC app milestone + Android smartphone app code

# Important notes



# TODO:
- See Trello

# COMPSYS700: Setup

The wfdb software package is required to run any python scripts that extract information from Physionet datasets. This is a standalone command line package, MATLAB package or Python package.

To easily download the datasets provided in this repo for yourself, use
`rsync`:
 
 `rsync -Cavz physionet.org::nameOfDb /directory`, where nameOfDb substitutes the desired database and /directory is the absolute path of where you want to save it.
