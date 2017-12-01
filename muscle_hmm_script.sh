#Muscle alignment for protein files from BLAST
#Path for muscle/hmmbuild may be different depending on where binaries are

for sequence in *.fasta
./muscle -in $sequence.fasta -out $sequence.align
