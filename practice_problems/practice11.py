def isValid(s):
    d = {'(':')','{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0

# from collections import Counter

# def firstUniqChar(s):
#     counts = Counter(s)
#     for i in range(len(s)):
#         if counts[s[i]] == 1:
#             return i
#     return -1
        
# s = "leetcode"
# print(firstUniqChar(s))

s = '()[]{}'
print(isValid(s))