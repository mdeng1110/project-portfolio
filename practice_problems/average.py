#list of numbers
nums = [2,4,6,8]

#loop through the list
for n in nums:
    print(n)

#function that sums elements in a list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

#function that finds the average of all the numbers in the list
def average(lst):
    len_of_lst = len(lst)
    total = 0
    for num in lst:
        total += num
    average = total/len_of_lst
    return average

#a function that returns the maximum value in a list (without using max()).
def find_max(lst):
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

#another function that prints all pairs of elements in a list (to see O(n²) behavior).
def pairs(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            result.append((lst[i], lst[j]))
    return result

print("Sum of List: ")
print(sum_list(nums))
print("Average of List: ")
print(int(average(nums)))
print("Maximum number: ")
print(find_max(nums))
print("Pairs")
print(pairs(nums))