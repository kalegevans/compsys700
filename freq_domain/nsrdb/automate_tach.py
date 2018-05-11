import os

# script requires wfdb console line package

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(1, 55):
    try:
        filename = 'corrected_' + str(i).zfill(3)
        freq = 128
        command = 'tach -r ' + filename + ' -a ecg -F ' + str(freq) + ' > '+ filename + 'rri.txt' # change 'ecg' to 'dat' depending on file format
        os.system(command)
    except:
        continue
