from hrv.classical import time_domain
from hrv.classical import non_linear
from hrv.utils import open_rri
# uses hrv package and converts dict output to csv format
import csv

 # how to use: td specifies td analysis and nl specifies NL analysis.
 # change it depending on which one you want output
specifier = 'td'

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(1, 55): # change range
    filename_header = 'nsr' + str(i).zfill(3) # change name possibly
    filename = filename_header + 'rri.txt'
    classifier = ''
    try:
        rri = open_rri(filename)
    except:
        continue

    if specifier == 'td':
        results = time_domain(rri) # output is dict
    elif specifier == 'nl':
        results = non_linear(rri)
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