""" 
This code converts the .dat ECG data from the MIT Arrthyhmia database into a more friendlier format, .csv

From this we can try and apply an algorithm to convert our ECG data into a RRI graph. RRI plots 
the intervals between heart beats (R-R intervals) over time, and all HRV metrics are derived from this.

Preliminary research has identified the Pan Tompkin's algorithm as something suitable for doing this conversion,
but anything goes. 
"""


import wfdb
import pandas as pd # for pandas data structure (can convert to csv)
import numpy as np
import glob # to read file list with shell commands


data_files=glob.glob('*.dat') #Get list of all .dat files
dataframe=pd.DataFrame(data=data_files)
dataframe.to_csv("files_list.csv",index=False,header=None) #Write list to a CSV file with no title axes
files=pd.read_csv("files_list.csv",header=None)

for i in range(1,len(files)):
	recordname=str(files.iloc[[i]]) # iloc = integer location, to access ith element
	recordname_new=str(recordname[-7:-4])#Extracting just the filename part, the 3 numbers
	record = wfdb.rdsamp(recordname_new) # rdsamp returns signal as a numpy array  
	record = np.asarray(record[0]) # process numpy array
	np.savetxt(recordname_new + ".csv",record,delimiter=",") #Write the CSV for each numpy array
	print("Files done: %s/%s"% (i,len(files)))
