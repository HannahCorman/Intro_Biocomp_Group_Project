## This script counts the number of lines "hits" for each group and each protein. This will create a new csv file for these hits which can be used to plot the hits in Python.
rm RNAseq_counts.csv
for cond in Control1 Control2 Obese1 Obese2; do
	for seq in Atp12a_8 Gsta2_1 Lhx2_9 Ptpn5_6 Slc7a12_2 Synpr_10; do
		count=$(cat "$cond"protein.fasta.$seq.out | grep -v "#" | wc -l)
		echo $cond,$seq,$count>>RNAseq_counts.csv
	done
done
