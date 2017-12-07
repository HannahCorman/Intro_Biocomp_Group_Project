#Group project graphing trial

#import packages
import numpy
import pandas
import scipy
import scipy.integrate as spint
from scipy.stats import norm
from scipy.optimize import minimize
from scipy.stats import chi2
from plotnine import *

#create single file with all output information
#Control 1 files condensed to 1 file
Control1filenames = ['control1protein.fasta.Atp12a_8.out','control1protein.fasta.Gsta2_1.out','control1protein.fasta.Lhx2_9.out','control1protein.fasta.Ptpn5_6.out','control1protein.fasta.Slc7a12_2.out','control1protein.fasta.Synpr_10.out']
with open('Control1hmmoutput', 'w') as outfile:
    for fname in Control1filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

#Control 2 files condensed to 1 file
Control2filenames = ['control2protein.fasta.Atp12a_8.out','control2protein.fasta.Synpr_10.out','control2protein.fasta.Slc7a12_2.out','control2protein.fasta.Ptpn5_6.out','control2protein.fasta.Lhx2_9.out','control2protein.fasta.Gsta2_1.out']
with open('Control2hmmoutput', 'w') as outfile:
    for fname in Control2filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                
#Obese 1 files condensed to 1 file 
Obese1filenames = ['obese1protein.fasta.Slc7a12_2.out','obese1protein.fasta.Atp12a_8.out','obese1protein.fasta.Ptpn5_6.out','obese1protein.fasta.Gsta2_1.out','obese1protein.fasta.Lhx2_9.out','obese1protein.fasta.Synpr_10.out']
with open('Obese1hmmoutput', 'w') as outfile:
    for fname in Obese1filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                
#Obese 2 files condensed to 1 file
Obese2filenames = ['obese2protein.fasta.Atp12a_8.out','obese2protein.fasta.Synpr_10.out','obese2protein.fasta.Slc7a12_2.out','obese2protein.fasta.Ptpn5_6.out','obese2protein.fasta.Lhx2_9.out','obese2protein.fasta.Gsta2_1.out']
with open('Obese2hmmoutput', 'w') as outfile:
    for fname in Obese2filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                
#Single file to use for graphing
ExpressionFiles = ['Control1hmmoutput','Control2hmmoutput','Obese1hmmoutput','Obese2hmmoutput']
with open('FinalHmmOutput', 'w') as outfile:
    for fname in ExpressionFiles:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

#Find number of hits in each treatment for each transcript
#load data
ExpressionData = pandas.read_csv("FinalHmmOutput",header=0,sep='\t')
#create an empty dataframe to put results in
ExpressionCounts = pandas.DataFrame(columns=['Group','Transcript','Number'])                
#Counter for Control1 transcripts
Control1Atp = Control1Gsta = Control1Lhx = Control1Ptpn = Control1S1c = Control1Synpr = 0
#Counter for Control2 transcripts
Control2Atp = Control2Gsta = Control2Lhx = Control2Ptpn = Control2S1c = Control2Synpr = 0
#Counter for Obese1 transcripts
Obese1Atp = Obese1Gsta = Obese1Lhx = Obeses1Ptpn = Obese1S1c = Obese1Synpr = 0
#Counter for Obese2 transcripts
Obese2Atp = Obese2Gsta = Obese2Lhx = Obese2Ptpn = Obese2S1c = Obese2Synpr = 0

#for loop to find the number of hits
for line in ExpressionData:
    line = line.strip()
    if line[0] == "Control1":
        if line[2] == "Atp12a_8.fasta":
            Control1Atp = Control1Atp+1
        elif line[2] == "Gsta2_1.fasta":
            Control1Gsta = Control1Gsta+1
        elif line[2] == "Lhx2_9.fasta":
            Control1Lhx = Control1Lhx+1
        elif line[2] == "Ptpn5_6.fasta":
            Control1Ptpn = Control1Ptpn+1
        elif line[2] == "Slc7a12_2.fasta":
            Control1S1c = Control1S1c+1
        else:
            Control1Synpr = Control1Synpr+1
    elif line[0] == "Control2":
        if line[2] == "Atp12a_8.fasta":
            Control2Atp = Control2Atp+1
        elif line[2] == "Gsta2_1.fasta":
            Control2Gsta = Control2Gsta+1
        elif line[2] == "Lhx2_9.fasta":
            Control2Lhx = Control2Lhx+1
        elif line[2] == "Ptpn5_6.fasta":
            Control2Ptpn = Control2Ptpn+1
        elif line[2] == "Slc7a12_2.fasta":
            Control2S1c = Control2S1c+1
        else:
            Control2Synpr = Control2Synpr+1
    elif line[0] == "Obese1":
        if line[2] == "Atp12a_8.fasta":
            Obese1Atp = Obese1Atp+1
        elif line[2] == "Gsta2_1.fasta":
            Obese1Gsta = Obese1Gsta+1
        elif line[2] == "Lhx2_9.fasta":
            Obese1Lhx = Obese1Lhx+1
        elif line[2] == "Ptpn5_6.fasta":
            Obese1Ptpn = Obese1Ptpn+1
        elif line[2] == "Slc7a12_2.fasta":
            Obese1S1c = Obese1S1c+1
        else:
            Obese1Synpr = Obese1Synpr+1
    else:
        if line[2] == "Atp12a_8.fasta":
            Obese2Atp = Obese2Atp+1
        elif line[2] == "Gsta2_1.fasta":
            Obese2Gsta = Obese2Gsta+1
        elif line[2] == "Lhx2_9.fasta":
            Obese2Lhx = Obese2Lhx+1
        elif line[2] == "Ptpn5_6.fasta":
            Obese2Ptpn = Obese2Ptpn+1
        elif line[2] == "Slc7a12_2.fasta":
            Obese2S1c = Obese2S1c+1
        else:
            Obese2Synpr = Obese2Synpr+1
            
            
#generate a summary plot - want to have 4 bars for each transcript
ggplot(expression,aes(x='',y=''))+geom_bar(stat="summary",fun_y=numpy.mean)+theme_classic()