import os

# script requires wfdb console line package

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(16265, 19831):
    try:
        filename = str(i)
        print("Converting: " + filename)
        command = 'tach -r ' + filename + ' -a nguess -F 128 > ' + filename + '_tach.txt'
        os.system(command)
    except:
        continue
