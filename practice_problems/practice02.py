#list of numbers
nums = [10,20,30,40,50]

def reverse_list(lst):
    n = len(lst)
    for i in range(n//2):
        lst[i], lst[n-1-i] = lst[n-1-i], lst[i]
    return lst

def find_second_largest_sorted(lst):
    if len(lst) < 2:
        return "List must contain at least two elements"
    sorted_nums = sorted(lst, reverse=True)
    return sorted_nums[1]

def rotate_left(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    return lst[k:] + lst[:k]

print("Original list:", nums)
reversed_list = reverse_list(nums)
print("Reversed list:", reversed_list)
second_largest = find_second_largest_sorted(nums)
print("Second Largest:", find_second_largest_sorted(nums))
rotated_list = rotate_left(nums, 2)
print("Rotated List:", rotated_list)
