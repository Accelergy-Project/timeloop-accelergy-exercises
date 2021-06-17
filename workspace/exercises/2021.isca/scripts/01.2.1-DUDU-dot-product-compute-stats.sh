printf "=== MAC ===\n\n"
grep "=== MAC ===" timeloop-model.stats.txt -A 20 | grep "A[a-z]* Computes"
grep "=== MAC ===" timeloop-model.stats.txt -A 20 | grep Cycles