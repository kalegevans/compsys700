from hrv.classical import time_domain
from hrv.classical import non_linear
from hrv.classical import frequency_domain
from hrv.utils import open_rri
from hrv.filters import moving_average
# uses hrv package and converts dict output to csv format
import csv

 # how to use: td specifies td analysis and nl specifies NL analysis.
 # change it depending on which one you want output
specifier = 'fd'

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(1, 55): # change range
    filename_header = 'nsr' + str(i).zfill(3) # change name possibly
    filename = filename_header + 'rri.txt'
    classifier = ''
    sample_freq = 128.0
    try:
        rri = open_rri(filename)
    except:
        continue

    if specifier == 'td':
        results = time_domain(rri) # output is dict
    elif specifier == 'nl':
        results = non_linear(rri)
    elif specifier == 'fd':
        results = frequency_domain(rri=rri, fs=4.0, method='welch', interp_method='cubic', detrend='linear')
    else:
        print("Invalid argument!")


    output_csv_name = filename_header + 'hrv_' + specifier + '.csv'
    with open(output_csv_name, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, results.keys())
        w.writeheader()
        w.writerow(results)
    
    print(filename_header + ' rri file has been processed')

""" print(results)
print(type(results)) """