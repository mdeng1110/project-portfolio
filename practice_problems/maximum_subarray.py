def max_subarray(a):
    
    size = len(a)
    
    previous_iteration_max = 0
    current_iteration_max = 0
    overall_max = 0

    for i in range(0, size):
        current_element = a[i]
        current_iteration_max = previous_iteration_max + current_element
        if current_iteration_max < 0:
            current_iteration_max = 0
        elif overall_max < current_iteration_max:
            overall_max = current_iteration_max
        previous_iteration_max = current_iteration_max

    return overall_max

print(max_subarray([-1,3,2,-2,1]))