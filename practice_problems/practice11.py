from collections import Counter

def firstUniqChar(s):
    counts = Counter(s)
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i
    return -1
        
s = "leetcode"
print(firstUniqChar(s))