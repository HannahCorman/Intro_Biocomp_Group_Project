#import packages
from __future__ import print_function
import sys

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
    for i, item in enumerate(fasta.read().split()):
        protein = '' # translated protein sequence
        if i%2 == 0: # if index is even
            sequence_names.append(item)
        else:
            started = False
            for j in range(0, len(item), 3):
                res = codex[item[j:j+3]]
                if res == 'M' and not started:
                    started = True
                    continue
                if started:
                    if res == 'Stop':
                        break
                    else:
                        protein += res
            sequences.append(protein)
    return '\n'.join(['{0}\n{1}\n'.format(sequence_names[p], sequences[p]) for p in range(len(sequences))])

if __name__ == '__main__':
    #read transcript fasta files
    try:
        condition_list = sys.argv[1:]
    	if not condition_list:
        	print('Usage: python Translate_RNA_SCript.py fasta1 fasta2... fastan')
        	sys.exit()
	    for condition in condition_list:
        	with open('%s.fasta'%condition, 'r') as inFile, \
	        open('%sprotein.fasta'%condition, 'w') as outFile:
        	    outFile.write(translate(d, inFile))
    except IOError:
       	print('Usage: python Translate_RNA_SCript.py fasta1 fasta2... fastan')
       	sys.exit()
	
