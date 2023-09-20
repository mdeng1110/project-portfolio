from sorting import *


def test_bubble_sort_ascending():
    test_input = [5, 4, 3 ,2, 1]
    bubble_sort = BubbleSort()
    assert(bubble_sort.sort(test_input)) == [1, 2, 3, 4, 5]


def test_bubble_sort_descending():
    test_input = [1, 2, 3, 4, 5]
    bubble_sort = BubbleSort()
    assert(bubble_sort.sort(test_input, sort_order='descending')) == [5, 4, 3 ,2, 1]


def test_selection_sort_ascending():
    test_input = [5, 4, 3 ,2, 1]
    selection_sort = SelectionSort()
    assert(selection_sort.sort(test_input)) == [1, 2, 3, 4, 5]


def test_selection_sort_descending():
    test_input = [1, 2, 3, 4, 5]
    selection_sort = SelectionSort()
    assert(selection_sort.sort(test_input, sort_order='descending')) == [5, 4, 3 ,2, 1]

# def test_insertion_sort_ascending():
#     test_input = [5, 4, 3 ,2, 1]
#     insertion_sort = InsertionSort()
#     assert(insertion_sort.sort()) == [1, 2, 3, 4, 5]


# def test_insertion_sort_descending():
#     test_input = [1, 2, 3, 4, 5]
#     insertion_sort = InsertionSort()
#     assert(insertion_sort.sort(sort_order='descending')) == [5, 4, 3 ,2, 1]


# def test_merge_sort_ascending():
#     test_input = [5, 4, 3 ,2, 1]
#     merge_sort = MergeSort()
#     assert(merge_sort.sort()) == [1, 2, 3, 4, 5]


# def test_merge_sort_descending():
#     test_input = [1, 2, 3, 4, 5]
#     merge_sort = MergeSort()
#     assert(merge_sort.sort(sort_order='descending')) == [5, 4, 3 ,2, 1]


# def test_quick_sort_ascending():
#     test_input = [5, 4, 3 ,2, 1]
#     quick_sort = QuickSort()
#     assert(quick_sort.sort()) == [1, 2, 3, 4, 5]


# def test_quick_sort_descending():
#     test_input = [1, 2, 3, 4, 5]
#     quick_sort = QuickSort()
#     assert(quick_sort.sort(sort_order='descending')) == [5, 4, 3 ,2, 1]


# def test_heap_sort_ascending():
#     test_input = [5, 4, 3 ,2, 1]
#     heap_sort = HeapSort()
#     assert(heap_sort.sort()) == [1, 2, 3, 4, 5]


# def test_heap_sort_descending():
#     test_input = [1, 2, 3, 4, 5]
#     heap_sort = HeapSort()
#     assert(heap_sort.sort(sort_order='descending')) == [5, 4, 3 ,2, 1]
