#import packages
from __future__ import print_function
import pandas
import os
import numpy
import csv

#open file codonmap and store it as a dictionary under the variable name "d"
d = {}
with open('codonmap.txt', 'r') as csv_file: # Soudn't open as binary, ASCII is fine.
    for line in csv_file:
        aa, codon = line.split() # Don't need parentheses for simultaneous assignment
        d[codon] = aa

def translate(d, fasta):
    """
    When passed a full fasta file split by line (i.e. file.read().split()),
    this function translates DNA to Protein up to an 
    Amber (TAG), Ochre (TAA), or Umber (TGA) stop codon.
    Returns a list of tab delimited NAME-SEQUENCE pairs.
    """
    sequences = [] # sequential list of protein sequences
    sequence_names = []
    for i, item in enumerate(fasta): # loops over list, list items
        protein = '' # translated protein sequence
        if i%2 == 0: # if index is even
            sequence_names.append(item)
        else:
            for j in range(0,len(y[1]),3):
                aa = d[item[j:j+3]]
                if aa == 'Stop':
                    break
                else:
                    protein += aa
            sequences.append(protein)
    return ['{0}\t{1}'.format(sequence_names[i], sequences[i]) for i in range(len(sequences))]

if __name__ == '__main__':
    #read transcript fasta files
    control1=open('control1.fasta', 'r')
    control2=open('control2.fasta', 'r')
    obese1=open('obese1.fasta', 'r')
    obese2=open('obese2.fasta', 'r')
    
    print('\n'.join(translate(d,control1.read().split())))
