#Files.py
#August 7th, 2022
#Caleb Freeman
#CIS 245
#Code that performs file processing 
import os
foldername = input('Enter folder name: ')
if os.path.isdir(foldername):
    filename = input('Enter file name: ') 
    file = foldername + "\\" + filename 
    name = input('Enter user name: ') 
    address = input('Enter address: ') 
    phone = input('Enter phone number: ')   
    out = open(file, 'w')
    print(f'{name},{address},{phone}', file=out)
    out.close()
    infile = open(file, 'r')
    data = infile.readline().strip().split(',')
    print(f'Your name: {data[0]}')
    print(f'Your address: {data[1]}')
    print(f'Your phone number: {data[2]}')
    infile.close()
else:
    print(f': {foldername} does not exist.')
  