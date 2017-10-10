cp $(printf '%s\n' *??????.txt | awk 'NR%2 == 1') subset_params/
