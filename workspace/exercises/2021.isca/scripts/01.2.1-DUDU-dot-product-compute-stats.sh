printf "=== MAC ===\n\n"
grep "=== MAC ===" timeloop-model.stats.txt -A 20 | grep Computes
grep "=== MAC ===" timeloop-model.stats.txt -A 20 | grep Cycles