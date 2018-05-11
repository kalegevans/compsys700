for i in range(16265, 19831): # i already did nsr001rri.txt manually
    try:
        filename = str(i) + 'rri.txt'
        with open(filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(filename, 'w') as fout:
            fout.writelines(data[1:])
        
        print(filename + " complete")
    except:
        continue