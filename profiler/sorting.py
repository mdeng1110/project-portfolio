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
    def sort(self, sort_order='ascending'):
        pass


class InsertionSort:
    def __init___(self):
        pass
    def sort(self, sort_order='ascending'):
        pass


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