def two_sum(arr, target):
    values = dict()

    for i, elem in enumerate(arr):
        comp = target - elem
        if comp in values:
            return [values[comp], i]
        values[elem] = i

    return []

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))