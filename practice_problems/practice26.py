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