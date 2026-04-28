def first_unique_char(s):
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

s = "aabbcdeff"
print(first_unique_char(s))