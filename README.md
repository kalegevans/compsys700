# COMPSYS700: Introdution
This is project #97 of the 2018 University of Auckland ECE Part IV projects. The intent of this research is
to provide an automated emergency callout system for heart disease patients in life threatening events. 

Our repository contains:
1. `/mitdb`, Code that investigates and processes MIT-BIH arrhythmia datasets into both non-linear and time-domain heart rate variability metrics - see https://physionet.org/tutorials/hrv-toolkit/#table1 for more information about these metrics. This process involves converting the ECG signal to the equivalent RRI signal, and then extrapolating HRV metrics from the RRI signal.
2. `/nsr2db`, similarly contains processed HRV metrics and datasets for normal sinus rhythm found here: https://www.physionet.org/physiobank/database/nsr2db/ (RRI processed already). There is `nsrdb` but again the datasets are really, really big. May do later.
3. `/svdb`, contains processed HRV metrics and datasets for supraventricular arrthyhmia.
4. `chf2db`, contains HRV metrics for congestive heart failure patients. This database gives us data already in RRI format, so conversion from ECG to RRI was not required. chfdb also exists but it is REALLY big so I didn't bother.
5. `/machinelearning`, Code that classifies our dataset into various heart disease states using a supervised learning algorithm 
6. `/smartphoneapp`, Code for an Android smartphone application that receives Bluetooth Low Energy heart rate data from a Polar H7 Belt
7. `/vfdb`, ventricular fibrillation db.

Popular datasets not included: nsrdb, chfdb (both are too large, combined is upwards of 1gb. May need to move off git)

# Important notes
In non-linear HRV analysis,
SD1 = the standard deviation of instantaneous beat-to-beat interval variability.
SD2 = the continuous long-term R/R interval variability

The ratios of SD1/SD2 are also considered, and the method of obtaining these is known as the Poincare Plot.


# TODO:
- See Trello

# COMPSYS700: Setup

The wfdb software package is required to run any python scripts that extract information from Physionet datasets. This is a standalone command line package, MATLAB package or Python package.

To easily download the datasets provided in this repo for yourself, simply install
`rsync` for downloading them all: use `rsync -Cavz physionet.org::nameOfDb /directory`, where nameOfDb substitutes the desired database and /directory is the absolute path of where you want to save it.
