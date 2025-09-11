from typing import List
def count_divisible_triplets(arr, d):
    n = len(arr)
    if n == 0:
        return 0
    if d <= 0:
        raise ValueError("d must be a positive integer")
    
    arr_mod = [x % d for x in arr]
    suffix_counts = [[0]*d for _ in range(n+1)]
    
    for pos in range(n-1, -1, -1):
        row = suffix_counts[pos+1]
        new_row = row.copy()
        new_row[arr_mod[pos]] += 1
        suffix_counts[pos] = new_row

    total = 0
    #iterate all i <= j pairs
    for i in range(n):
        for j in range(i, n):
            need = (-(arr_mod[i] + arr_mod[j])) % d
            total += suffix_counts[j][need]
    return total





arr = [1, 2, 3, 4]
d = 3
print(count_divisible_triplets(arr, d))