#Graphing using the bash script/text files so that we have something

#import packages
import numpy
import pandas
import scipy
import scipy.integrate as spint
from scipy.stats import norm
from scipy.optimize import minimize
from scipy.stats import chi2
from plotnine import *

#load data
expression = pandas.read_csv("Expression_data.txt",header=0,sep=",")

#Summary plot give information as a whole - doesn't separate out by treatment
ggplot(expression,aes(x='Transcript',y='Count'))+geom_bar(stat="summary",fun_y=numpy.mean)+theme_classic()
#Plot to separate out by treatment
ggplot(expression,aes(x='Transcript',fill='Group',y='Count'))+geom_bar(stat="summary",fun_y=numpy.mean)
