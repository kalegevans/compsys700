import os

# script requires wfdb console line package

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(1, 55):
    try:
        filename = 'nsr' + str(i).zfill(3)
        command = 'nguess -r ' + filename + '-a ecg ' + '-o' + ' corrected_' + filename + '.atr'
        os.system(command)
    except:
        continue
