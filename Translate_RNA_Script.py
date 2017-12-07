"""
Translates all DNA sequences in an arbitrary number of fasta files
into amino acids. Takes fasta file names as command line arguments,
WITHOUT any extension:

USAGE: python Translate_RNA_Script.py fasta1 fasta2 ... fastan

Cannot be run using the run script button in Rodeo or Spyder.
Try running in a terminal.
"""
from __future__ import print_function
import sys

# creates dictionary which contains DNA codon-to-amino acid translations
D = {}
with open('codonmap.txt', 'r') as csv_file:
    for line in csv_file:
        aa, codon = line.split()
        D[codon] = aa

def translate(codex, fasta):
    """
    When passed a full fasta file split by line (i.e. file.read().split()),
    this function translates DNA to Protein up to an
    Amber (TAG), Ochre (TAA), or Umber (TGA) stop codon.
    Returns a list of tab delimited NAME-SEQUENCE pairs.
    """
    sequences = [] # sequential list of protein sequences
    sequence_names = []
    for i, item in enumerate(fasta.read().split()):
        protein = '' # translated protein sequence
        if i%2 == 0: # if index is even, line is seq name
            sequence_names.append(item)
        else: # otherwise, fasta is DNA sequence
            started = False # Initiating met. hasn't been found.
            for j in range(0, len(item), 3): # read by 3s
                res = codex[item[j:j+3]]
                if res == 'M' and not started:
                    started = True # start translating if we find a met.
                    continue
                if started:
                    if res == 'Stop': # stop codon, end translation
                        break
                    else:
                        protein += res # extend translated protein seq.
            sequences.append(protein)
    # return names followed by sequences line-by-line
    return '\n'.join(['{0}\n{1}\n'.format(sequence_names[p],
                                          sequences[p]) for p in range(len(sequences))])

if __name__ == '__main__':
    #read transcript fasta files from system arguments
    try:
        CONDITION_LIST = ['control1', 'control2', 'obese1', 'obese2']
        for condition in CONDITION_LIST:
            with open('fasta/%s.fasta'%condition, 'r') as inFile, \
                open('%sprotein.fasta'%condition.title(), 'w') as outFile:
                # translates and auto-closes both input and output file
                outFile.write(translate(D, inFile))
    except IOError: # If no arguments passed, exit and print error.
        print('Usage: python Translate_RNA_SCript.py fasta1 fasta2... fastan')
        sys.exit()
