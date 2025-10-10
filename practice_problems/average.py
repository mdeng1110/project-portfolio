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

print("Sum of List: ")
print(sum_list(nums))
print("Average of List")
print(int(average(nums)))