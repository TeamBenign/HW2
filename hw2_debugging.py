"""Merge sort module"""


def merge_sort(arr):
    """Merge sort function that returns a sorted array"""
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if any(not isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements in the list must be integers or floats")

    if len(arr)     <=    1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """combine or merge two lists"""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1
    return                         merge_arr

# Remove to run pytest
# arr = rand.random_array([None] * 20)
# arr_out = merge_sort(arr)

# print(arr_out)
