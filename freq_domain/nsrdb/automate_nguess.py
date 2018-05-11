import os

# script requires wfdb console line package

# this script is GENERAL purpose. you need to change some of these to match the filenames


for i in range(16265, 19831):
    try:
        filename = str(i)
        command = 'nguess -r ' + filename + '-a atr '
        os.system(command)
    except:
        continue
