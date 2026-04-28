def group_anagrams(s):
    groups = {}
    for word in s:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(s))
