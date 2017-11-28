## This script will take the top line or "hit" from each .csv file in 
## the directory and compile them into a new .txt file called 
## "tophits.txt"

for file in Alignments
do
head -n 1 *.csv > tophits.txt
done
