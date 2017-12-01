#import packages
from __future__ import print_function
import csv
import os
import pandas
import numpy


#open file codonmap and store it as a dictionary under the variable name "d"
d = {}
with open('codonmap.txt', 'r') as csv_file: # Soudn't open as binary, ASCII is fine.
    for line in csv_file:
        aa, codon = line.split() # Don't need parentheses for simultaneous assignment
        d[codon] = aa

def translate(codex, fasta):
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
            for j in range(0, len(item), 3):
                res = codex[item[j:j+3]]
                if res == 'Stop':
                    break
                else:
                    protein += res
            sequences.append(protein)
    return ['{0}\n{1}'.format(sequence_names[p], sequences[p]) for p in range(len(sequences))]

if __name__ == '__main__':
    #read transcript fasta files
    control1 = open('control1.fasta', 'r')
    control2 = open('control2.fasta', 'r')
    obese1 = open('obese1.fasta', 'r')
    obese2 = open('obese2.fasta', 'r')
    #creates and opens files to write
    control1protein = open('control1protein.fasta', 'w')
    control2protein = open('control2protein.fasta', 'w')
    obese1protein = open('obese1protein.fasta', 'w')
    obese2protein = open('obese2protein.fasta', 'w')
    #writes the translated nucleotides to the outfiles
    control1protein.write('\n'.join(translate(d, control1.read().split())))
    control2protein.write('\n'.join(translate(d, control2.read().split())))
    obese1protein.write('\n'.join(translate(d, obese1.read().split())))
    obese2protein.write('\n'.join(translate(d, obese2.read().split())))
    #closes files
    control1.close
    control2.close
    obese1.close
    obese2.close
    control1protein.close
    control2protein.close
    obese1protein.close
    obese2protein.close
    
    
