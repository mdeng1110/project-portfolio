def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    return result

nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))