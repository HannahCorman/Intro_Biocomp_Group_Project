#Bash script to get expression counts. Can make this final code version if we can't get for loop to work.

rm Expression_data.txt
for cond in "Control1" "Control2" "Obese1" "Obese2"; do
	for seq in "Atp12a_8.fasta" "Gsta2_1.fasta" "Lhx2_9.fasta" "Ptpn5_6.fasta" "S1c7a12_2.fasta" "Synpr_10.fasta"; do
		count=$(grep $cond FinalHmmOutput | grep $seq | wc -l)
		seq_name=$(echo $seq | cut -d '.' -f 1)
		echo "$cond,$seq_name,$count" >> Expression_data.txt
	done
done
