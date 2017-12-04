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

for build in $(ls | egrep 'protein.fasta$') #grep only protein.fasta files
	do
	./hmmsearch --tblout $build.Atp12a_8.out Atp12a_8.fasta.align.hmm $build  
	./hmmsearch --tblout $build.Gsta2_1.out Gsta2_1.fasta.align.hmm $build
	./hmmsearch --tblout $build.Lhx2_9.out Lhx2_9.fasta.align.hmm $build
	./hmmsearch --tblout $build.Ptpn5_6.out Ptpn5_6.fasta.align.hmm $build
	./hmmsearch --tblout $build.Slc7a12_2.out Slc7a12_2.fasta.align.hmm $build
	./hmmsearch --tblout $build.Synpr_10.out Synpr.fasta.align.hmm $build
	done
