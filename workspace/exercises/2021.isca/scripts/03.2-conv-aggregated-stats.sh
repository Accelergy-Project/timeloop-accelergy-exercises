

printf "\n=== BackingStorage ===\n"
printf "\n --- Weights --- \n"
grep "=== BackingStorage" *.stats.txt -A 80 | grep "Weights:" -A 80 | grep -e 'shape' -e ' storage c' -e 'format' \
-e reads


printf "\n=== Buffer ===\n"
printf "\n --- Weights --- \n"
grep "=== Buffer" *.stats.txt -A 80 | grep -e 'shape' -e ' storage c' -e 'format' -e reads -e fills

printf "\n --- Inputs  --- \n"
grep "=== Buffer" *.stats.txt -A 120 | grep "Inputs:" -A 80 | grep -e 'shape' -e 'storage c' -e 'Skipped scalar reads' -e 'scalar fills'


printf "\n --- Outputs --- \n"
grep "=== Buffer" *.stats.txt -A 170 | grep "Outputs:" -A 80 | grep -e 'shape' -e 'data storage c' -e 'A[a-z]* scalar [reads|updates]' \
 -e 'Skipped scalar [reads|updates]'

echo ""

printf "=== MAC ===\n\n"
grep "=== MAC ===" timeloop-model.stats.txt -A 20 | grep "A[a-z]* Computes"
grep "=== MAC ===" timeloop-model.stats.txt -A 20 | grep Cycles

echo ""

printf "=== Summary Stats ===\n\n"
grep "Summary Stats" timeloop-model.stats.txt -B 8 | grep topology
echo " "
grep "Summary Stats" timeloop-model.stats.txt -A 50 | grep "Algorithmic Computes" -A 40 | grep -v "<==>"