def isValid(s):
    d = {'(':')','{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0

def reverseString(s):
    n = len(s)
    l = 0
    r = n - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

# from collections import Counter

# def firstUniqChar(s):
#     counts = Counter(s)
#     for i in range(len(s)):
#         if counts[s[i]] == 1:
#             return i
#     return -1
        
# s = "leetcode"
# print(firstUniqChar(s))

# s = '()[]{}'
# print(isValid(s))

s = ["h","e","l","l","o"]
print(reverseString(s))