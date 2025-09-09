def max_subarray(a):
    curr = best = a[0]
    for x in a[1:]:
        curr = max(x, curr +x)
        best = max(best, curr)
    return best

print(max_subarray([-1,3,2,-2,1]))