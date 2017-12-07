#!/bin/bash
#Muscle alignment for protein files from BLAST
#Build hmm for alignments
#Path for muscle/hmmbuild may be different depending on where binaries are

for sequence in $(ls | egrep '_[0-9]{1,2}\.fasta$'); do
	./align/muscle.exe -in $sequence -out ./align/$sequence.align
done

for alignment in $(ls ./align/ | egrep '_[0-9]{1,2}\.fasta.align$'); do
	./hmm/hmmbuild ./hmm/$alignment.hmm ./align/$alignment
done

for build in $(ls | egrep 'protein.fasta$'); do
	for seq in "Atp12a_8" "Gsta2_1" "Lhx2_9" "Ptpn5_6" "Slc7a12_2" "Synpr_10"; do
		./hmm/hmmsearch --tblout ./hmmoutput/$build.$seq.out ./hmm/$seq.fasta.align.hmm ./$build
	done
done
