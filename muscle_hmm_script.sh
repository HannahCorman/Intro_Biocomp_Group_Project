#Muscle alignment for protein files from BLAST
#Path for muscle/hmmbuild may be different depending on where binaries are

for sequence in $(ls | egrep '_[0-9]{1,2}\.fasta')
	do ./muscle -in $sequence -out $sequence.align
	done

