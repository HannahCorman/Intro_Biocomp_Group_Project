import pandas

c=pandas.read_csv("RNAseq_counts.csv", sep=',', names = ["Condition","Sequence","Count"])