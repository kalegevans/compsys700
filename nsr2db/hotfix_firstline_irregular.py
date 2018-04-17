for i in range(2, 55): # i already did nsr001rri.txt manually
    filename = 'nsr' + str(i).zfill(3) + 'rri.txt'
    with open(filename, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(filename, 'w') as fout:
        fout.writelines(data[1:])
    
    print(filename + " complete")