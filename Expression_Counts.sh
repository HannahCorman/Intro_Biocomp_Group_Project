#Bash script to get expression counts. Can make this final code version if we can't get for loop to work.

cat FinalHmmOutput | grep -e "Control1" | grep -e "Atp12a_8.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control1" | grep -e "Gsta2_1.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control1" | grep -e "Lhx2_9.fasta" | wc -l >>Expression_data
cat FinalHmmOutput | grep -e "Control1" | grep -e "Ptpn5_6.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control1" | grep -e "S1c7a12_2.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control1" | grep -e "Synpr_10.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control2" | grep -e "Atp12a_8.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control2" | grep -e "Gsta2_1.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control2" | grep -e "Lhx2_9.fasta" | wc -l >>Expression_data
cat FinalHmmOutput | grep -e "Control2" | grep -e "Ptpn5_6.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control2" | grep -e "S1c7a12_2.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Control2" | grep -e "Synpr_10.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese1" | grep -e "Atp12a_8.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese1" | grep -e "Gsta2_1.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese1" | grep -e "Lhx2_9.fasta" | wc -l >>Expression_data
cat FinalHmmOutput | grep -e "Obese1" | grep -e "Ptpn5_6.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese1" | grep -e "S1c7a12_2.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese1" | grep -e "Synpr_10.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese2" | grep -e "Atp12a_8.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese2" | grep -e "Gsta2_1.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese2" | grep -e "Lhx2_9.fasta" | wc -l >>Expression_data
cat FinalHmmOutput | grep -e "Obese2" | grep -e "Ptpn5_6.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese2" | grep -e "S1c7a12_2.fasta" | wc -l >> Expression_data
cat FinalHmmOutput | grep -e "Obese2" | grep -e "Synpr_10.fasta" | wc -l >> Expression_data



