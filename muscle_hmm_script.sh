#Muscle alignment for protein files from BLAST
#Build hmm for alignments
#Path for muscle/hmmbuild may be different depending on where binaries are

for sequence in $(ls | egrep '_[0-9]{1,2}\.fasta$') #grep only fasta files from BLAST search, not translated RNAseq files
	do 
	./muscle -in $sequence -out $sequence.align
	done

for alignment in $(ls | egrep '_[0-9]{1,2}\.fasta.align$') #grep only alignment files
	do
	./hmmbuild $alignment.hmm $alignment
	done
