def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    leftHalf = lst[:mid]
    rightHalf = lst[mid:]
    
    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [46, 3, 8 , 9, 3, 2, 4, 9]
print("Original: ", nums)
print("Sorted: ", merge_sort(nums))
