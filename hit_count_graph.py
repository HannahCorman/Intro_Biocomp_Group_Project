import pandas
from plotnine import *
c=pandas.read_csv("hmmoutput/RNAseq_counts.csv", sep=',', names = ["Condition","Sequence","Count"])

plot = (ggplot(c,aes(x='Condition',y='Count',fill='Sequence'))+geom_bar(stat='identity',position='dodge')+ggtitle("Hit Counts"))
print(plot)