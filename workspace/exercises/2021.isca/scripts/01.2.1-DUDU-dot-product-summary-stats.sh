printf "=== Summary Stats ===\n\n"
grep "Summary Stats" timeloop-model.stats.txt -B 8 | grep topology
echo " "
grep "Summary Stats" timeloop-model.stats.txt -A 50 | grep "Computes" -A 40 | grep -v "<==>"
