import multiprocessing
import random 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

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

def parallel_merge_sort(arr, processes):
    if len(arr) <= 1:
        return arr

    size = len(arr) // processes
    chunks = [arr[i:i + size] for i in range(0, len(arr), size)]

    with multiprocessing.Pool(processes) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    result = sorted_chunks[0]
    for i in range(1, len(sorted_chunks)):
        result = merge(result, sorted_chunks[i])

    return result

if __name__ == "__main__":
    input_list = [4, 2, 8, 6, 5, 1, 7, 3]
    sorted_list = parallel_merge_sort(input_list, 2)

    print("Unsorted list: ", input_list)
    print("Sorted list: ", sorted_list)