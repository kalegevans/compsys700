from hrv.classical import time_domain
from hrv.utils import open_rri
# uses hrv package and converts dict output to csv format
import csv

for i in range(100, 235):
    filename_header = str(i)
    filename = filename_header + 'rri.txt'
    try:
        rri = open_rri(filename)
    except:
        continue

    td_results = time_domain(rri) # output is dict
    output_csv_name = filename_header + 'hrv_td.csv'

    with open(output_csv_name, 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, td_results.keys())
        w.writeheader()
        w.writerow(td_results)
    
    print(filename_header + ' rri file has been processed')

""" print(td_results)
print(type(td_results)) """