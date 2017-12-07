#Group project graphing trial

#import packages
import os
import numpy
import pandas
import scipy
import scipy.integrate as spint
from scipy.stats import norm
from scipy.optimize import minimize
from scipy.stats import chi2
from plotnine import *

CONDITIONS = ['Control1', 'Control2', 'Obese1', 'Obese2']
SEQ_NAMES = ['Atp12a_8','Gsta2_1','Lhx2_9','Ptpn5_6','Slc7a12_2','Synpr_10']

def condense_output(cond):
    """ Condenses output of all Hmmsearches for each condition to a single file.
    """
    filenames = ['{0}protein.fasta.{1}.out'.format(cond, seq) for seq in SEQ_NAMES]
    with open('%shmmoutput'%cond, 'w') as outFile:
        for f in filenames:
            with open('./hmmoutput/%s'%f, 'r') as inFile:
                outFile.write(inFile.read())

#create single file with all output information
#Control 1 files condensed to 1 file
[condense_output(cond) for cond in CONDITIONS]
                
#Single file to use for graphing

#Find number of hits in each treatment for each transcript
#load data
FinalHmmOutput = open("FinalHmmOutput", "r")

#create an empty dataframe to put results in
ExpressionCounts = pandas.DataFrame(columns=['Group','Transcript','Number'])
ExpressionData = [line.strip() for line in FinalHmmOutput.read().split('\n')]

#Counter for Control1 transcripts
Control1Atp = Control1Gsta = Control1Lhx = Control1Ptpn = Control1S1c = Control1Synpr = 0
#Counter for Control2 transcripts
Control2Atp = Control2Gsta = Control2Lhx = Control2Ptpn = Control2S1c = Control2Synpr = 0
#Counter for Obese1 transcripts
Obese1Atp = Obese1Gsta = Obese1Lhx = Obese1Ptpn = Obese1S1c = Obese1Synpr = 0
#Counter for Obese2 transcripts
Obese2Atp = Obese2Gsta = Obese2Lhx = Obese2Ptpn = Obese2S1c = Obese2Synpr = 0

#for loop to find the number of hits
for line in ExpressionData:
    line = line.strip()
    if "Control1" in line:
        if "Atp12a_8.fasta" in line:
            Control1Atp += 1
        elif "Gsta2_1.fasta" in line:
            Control1Gsta += 1
        elif "Lhx2_9.fasta" in line:
            Control1Lhx += 1
        elif "Ptpn5_6.fasta" in line:
            Control1Ptpn += 1
        elif "Slc7a12_2.fasta" in line:
            Control1S1c += 1
        else:
            Control1Synpr += 1
    elif "Control2" in line:
        if "Atp12a_8.fasta" in line:
            Control2Atp += 1
        elif "Gsta2_1.fasta" in line:
            Control2Gsta += 1
        elif "Lhx2_9.fasta" in line:
            Control2Lhx += 1
        elif "Ptpn5_6.fasta" in line:
            Control2Ptpn += 1
        elif "Slc7a12_2.fasta" in line:
            Control2S1c += 1
        else:
            Control2Synpr += 1
    elif "Obese1" in line:
        if "Atp12a_8.fasta" in line:
            Obese1Atp += 1
        elif "Gsta2_1.fasta" in line:
            Obese1Gsta += 1
        elif "Lhx2_9.fasta" in line:
            Obese1Lhx += 1
        elif "Ptpn5_6.fasta" in line:
            Obese1Ptpn += 1
        elif "Slc7a12_2.fasta" in line:
            Obese1S1c += 1
        else:
            Obese1Synpr += 1
    else:
        if "Atp12a_8.fasta" in line:
            Obese2Atp += 1
        elif "Gsta2_1.fasta" in line:
            Obese2Gsta += 1
        elif "Lhx2_9.fasta" in line:
            Obese2Lhx += 1
        elif "Ptpn5_6.fasta" in line:
            Obese2Ptpn += 1
        elif "Slc7a12_2.fasta" in line:
            Obese2S1c += 1
        else:
            Obese2Synpr += 1
            
            
#generate a summary plot - want to have 4 bars for each transcript
ggplot(expression,aes(x='',y=''))+geom_bar(stat="summary",fun_y=numpy.mean)+theme_classic()
