import rand


def mergeSort(arr):

    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if any(not isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements in the list must be integers or floats")

    if (len(arr) <= 1):
        return arr

    half = len(arr) // 2
    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]
        leftIndex += 1

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
        rightIndex += 1
    return mergeArr

# Remove to run pytest
# arr = rand.random_array([None] * 20)
# arr_out = mergeSort(arr)

# print(arr_out)
