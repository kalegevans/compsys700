import os

# script requires wfdb console line package

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(1, 55):
    try:
        filename = 'r' + str(i).zfill(3)
        command = 'ann2rr -r ' + filename + ' -a atr >' + filename + 'rri.txt' # change 'ecg' to 'dat' depending on file format
        os.system(command)
    except:
        continue
