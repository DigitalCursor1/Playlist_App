# Levenshtein can compare string similarity, some good tuning should remove the issue with duplicate songs from different authors.
import Levenshtein

original_list = ["Usater", "Large Song- by sintow", ]
new_list = ["Srutea", "sintow - large song"]

for i in new_list:
    for b in original_list:
        ratio = Levenshtein.ratio(original_list[b],new_list[i])
        print(original_list[b]+":"+new_list[i]+":"+ratio + "%\n")