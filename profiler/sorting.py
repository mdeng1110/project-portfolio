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
    def __init__(self, nums):
        self.nums = nums


    def merge(self, L, R, l, r):
        #ascending
        # temp = []
        for i in range(len(L)):
            # print(f'L[{i}]: ', L[i])
            # print(f'R[{i}]: ', R[i])
            if L[i] > R[i]:
                self.nums[l+i] = R[i]
                # temp.append(R[i])
                # temp.append(L[i])
                self.nums[r+i] = L[i]
            else:
                self.nums[r+i] = L[i]
                self.nums[l+i] = R[i]
                # temp.append(L[i])
                # temp.append(R[i])
        # print('TEMP: ', temp)
        # self.nums = temp
        print('NUMS: ', self.nums)
        #descending

    def sort(self, sort_order='ascending'):
        p = 1
        count = 0
        while p < len(self.nums):  
            for i in range(0, len(self.nums) - 1, p):       
                l = min(i + (p * i), len(self.nums) - 1)
                r = min(((l+p) + 1) - 1, len(self.nums) - 1)
                L = self.nums[l:l+p]
                R = self.nums[r:r+p]
                if l == r:
                    R = None
                    break
                self.merge(L, R, l, r)
            count += 1
            p = 2**count
        if sort_order == 'ascending':
            pass 
        elif sort_order == 'descending':
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