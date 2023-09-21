class BubbleSort:
    def __init___(self):
        pass
    def sort(self, nums, sort_order='ascending'):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if sort_order == 'ascending':
                    if nums[j] > nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                elif sort_order == 'descending':
                    if nums[j] < nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
        return nums


class SelectionSort:
    def __init___(self):
        pass
    def sort(self, nums, sort_order='ascending'):
        for i in range(len(nums)):
            min_ind = i
            for j in range(i, len(nums) - i):
                if sort_order == 'ascending':
                    if nums[min_ind] > nums[j]:
                        min_ind = j
                elif sort_order == 'descending':
                    if nums[min_ind] < nums[j]:
                        min_ind = j
            nums[i], nums[min_ind] = nums[min_ind], nums[i]
        return nums

class InsertionSort:
    def __init___(self):
        pass
    def sort(self, nums, sort_order='ascending'):
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if sort_order == 'ascending':
                    if nums[j - 1] > nums[j]:
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
                elif sort_order == 'descending':
                    if nums[j - 1] < nums[j]:
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

class MergeSort:
    def __init___(self):
        pass
    def sort(self, sort_order='ascending'):
        pass


class QuickSort:
    def __init___(self):
        pass
    def sort(self, sort_order='ascending'):
        pass        


class HeapSort:
    def __init___(self):
        pass
    def sort(self, sort_order='ascending'):
        pass