printf "\n=== Buffer ===\n"
printf "\n --- A --- \n"
grep "=== Buffer" *.stats.txt -A 80 | grep -e 'shape' -e ' data storage c' -e 'A[a-z]* scalar reads'
printf "\n --- B --- \n"
grep "=== Buffer" *.stats.txt -A 120 | grep "B:" -A 80 | grep -e 'shape' -e 'data storage c' -e 'A[a-z]* scalar reads'
printf "\n --- Z --- \n"
grep "=== Buffer" *.stats.txt -A 170 | grep "Z:" -A 80 | grep -e 'shape' -e 'data storage c' -e 'A[a-z]* scalar [reads|updates]'