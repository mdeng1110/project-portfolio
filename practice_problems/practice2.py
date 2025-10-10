#list of numbers
nums = [10,20,30,40,50]

#loop through the list
# for n in nums:
#     print(n)

def reverse_list(lst):
    n = len(lst)
    for i in range(n//2):
        lst[i], lst[n-1-i] = lst[n-1-i], lst[i]
    return lst

# def second_largest(lst):

print("Original list:", nums)
reversed_list = reverse_list(nums)
print("Reversed list:", reversed_list)
