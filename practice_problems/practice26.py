# Practice Problem #1: Count Occurences
def count_occurrences(nums):
    result = {}
    for num in nums:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1
    return result

nums = [1,1,2,3,3,3]
# Print Count Occurrences
print(count_occurrences(nums))

# Practice Problem #2: Find Duplicates
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Print Find Duplicates
print(find_duplicates(nums))

# Practice Question #3
def reverse_string(text):
    return text[::-1]

text="hello"
print(reverse_string(text))

# Practice Question 4: Palindrome
def is_palindrome(text1):
    text1 = text1.lower()
    return text1 == text1[::-1]

text1 = "tacocat"
print(is_palindrome(text1))