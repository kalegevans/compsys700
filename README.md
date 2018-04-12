# COMPSYS700: Introdution
This is project #97 of the 2018 University of Auckland ECE Part IV projects. The intent of this research is
to provide an automated emergency callout system for heart disease patients in life threatening events. 

Our repository contains:
1. Code that investigates and processes MIT-BIH arrhythmia datasets into a various time-domain heart rate variability metrics - see https://physionet.org/tutorials/hrv-toolkit/#table1 for more information about these metrics.
2. Code that classifies our dataset into various heart disease states using a supervised learning algorithm 
3. Code for an Android smartphone application that receives Bluetooth Low Energy heart rate data from a Polar H7 Belt

# COMPSYS700: Setup
This project is dependant on the wfdb repository, use:
```pip install wfdb```
