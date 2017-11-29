#import packages
import pandas
import os
import numpy 
import csv 
#open file codonmap and store it as a dictionary under the variable name "d"
d = {}
with open('codonmap.txt', 'rb') as csv_file:
    for line in csv_file:
        (key, val) = line.split()
        d[val] = key

print(d)
#read transcript fasta files
control1=open('control1.fasta', 'r')
control2=open('control2.fasta', 'r')
obese1=open('obese1.fasta', 'r')
obese2=open('obese2.fasta', 'r')

