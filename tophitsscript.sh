## This script will take the top line or "hit" from each .csv file in
## the directory and compile them into a new .txt file called
## "tophits.txt"

head -n 1 ./BLAST/*.csv > ./BLAST/tophits.txt