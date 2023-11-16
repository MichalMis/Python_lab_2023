import os 
import sys
import random 

def sorting_one(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j + 1] = temp 
    print (numbers)

def partition(arr, start, end):
    pivot = arr[start]
    count = 0
    for i in range(start+1, end+1):
        if arr[i] <= pivot:
            count += 1
    pivotIndex = start + count
    arr[pivotIndex], arr[start] = arr[start], arr[pivotIndex]
    i, j = start, end
    while i < pivotIndex and j > pivotIndex:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < pivotIndex and j > pivotIndex:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return pivotIndex

def sorting_two(arr, start, end):
    if start >= end:
        return
    p = partition(arr, start, end)
    sorting_two(arr, start, p - 1)
    sorting_two(arr, p + 1, end)
 
def main():
    numbers = []
    for i in range(10):
        rand_num = 10 * random.random()
        numbers.append(rand_num)
    print(numbers)
    sorting_one(numbers)
    sorting_two(numbers, 0, len(numbers) - 1)
    print(numbers)

if __name__ == '__main__':
    sys.exit(main())