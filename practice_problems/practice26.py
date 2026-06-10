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

# Practice Question #5: FizzBuzz
for i in range(1, 50):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Python #1
def frequency(text_list):
    word_counts = {}
    word_list = text_list.split()
    for text in word_list:
        if text not in word_counts:
            word_counts[text] = 1
        else:
            word_counts[text] += 1
    return word_counts
text_list = "apple banana apple orange banana apple"
print(frequency(text_list))

# Python #2
def nonrepeating(word):
    char_dict = {}
    for char in word:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    for k, v in char_dict.items():
        if v == 1:
            return k
word = "swiss"
print(nonrepeating(word))

# Python 3: Find the Largest Number
def largest_num(nums1):
    max_num = nums1[0]
    for num in nums1:
        if num > max_num:
            max_num = num
    return max_num
nums1 = [12, 5, 27, 3, 18]
print(largest_num(nums1))

# Python 4: Find the Smallest Number
def smallest_num(nums2):
    min_num = nums2[0]
    for num in nums2:
        if num < min_num:
            min_num = num
    return min_num
nums2 = [12, 5, 27, 3, 18]
print(smallest_num(nums2))

print(largest_num(nums1), smallest_num(nums1))

# Reverse a string
def reverse(text2):
    return text2[::-1]
def reverse2(text2):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text
text2 = "python"
print(reverse(text2))

# Python Problem: Find Duplicates in a List
def duplicates_nums(nums3):
    nums_dict = {}
    result = []
    for num in nums3:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
    for k, v in nums_dict.items():
        if v > 1:
            result.append(k)
    return result
nums3 = [1, 2, 2, 3, 4, 4, 5]
print(duplicates_nums(nums3))

# List Comprehension Practice
nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [i for i in nums4 if i % 2 == 0]

print(result)