#import packages
import pandas
import os
import numpy 
import csv 
#open file codonmap and store it as a dictgionary under the variable name "d"
d = {}
with open('codonmap.txt', 'rb') as csv_file:
    for line in csv_file:
        (key, val) = line.split()
        d[val] = key

print(d)
#read unique transcripts fasta file 

    