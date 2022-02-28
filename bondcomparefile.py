#Code to compare bond file size and append in csv
import os
import csv
from csv import DictWriter
from os import listdir
from os.path import isfile
dict1 = {}
dict2 = {}
prod = "C:/Users/Sandesh Vora/OneDrive/Desktop/folder1"
reg = "C:/Users/Sandesh Vora/OneDrive/Desktop/folder2"
prodfiles = [files for files in listdir(prod) if isfile]
for file in prodfiles:
    dict1[file] = os.path.getsize(file)
regfiles = [files for files in listdir(reg) if isfile]
for file in regfiles:
    dict2[file] = os.path.getsize(file)
print(dict1)
print(dict2)
new_csv = 'C:/Users/Sandesh Vora/OneDrive/Desktop/BondResults.csv'
with open(new_csv,'w') as f:
    for key1,value1 in dict1.items():
        for key2,value2 in dict2.items():
            if key1 == key2:
                if value1 == value2:
                    f.write(key1)
                    f.write(value1)
                    print("TRUE")
                else:
                    f.write(key2)
                    print("FALSE")
