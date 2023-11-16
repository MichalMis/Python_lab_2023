import os 
import sys
import random 
import multiprocessing
from multiprocessing import Pool
import matplotlib.pyplot as plt
from timeit import default_timer as timer

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
        return arr
    p = partition(arr, start, end)
    sorting_two(arr, start, p - 1)
    sorting_two(arr, p + 1, end)
    return arr
 

def sorting_alghoritm(proc_num, input_size):
    numbers = []
    for i in range(input_size):
        rand_num = 10 * random.random()
        numbers.append(rand_num)
    
    print(numbers)
    processes = proc_num
    start = timer()
    with multiprocessing.Pool(processes) as pool:
        start, end = 0, len(numbers) - 1
        items = [(numbers, start, end)]
        sorted_chunks = pool.starmap(sorting_two,items)
    end = timer()
    time = end - start 
    #print(time)
    #print (sorted_chunks)
    return time 
    
    # lenght = []
    # for i in range(3):
    #     lenght.append(i)
    
    # processes2 = 4
    # start1 = timer()
    # with multiprocessing.Pool(processes2) as pool:
    #     start, end = 0, len(numbers) - 1
    #     items = [(numbers, start, end)]
    #     sorted_chunks = pool.starmap(sorting_two,items)
    # end1 = timer()
    # time1 = end1 - start1 

    # processes3 = 8
    # start2 = timer()
    # with multiprocessing.Pool(processes3) as pool:
    #     start, end = 0, len(numbers) - 1
    #     items = [(numbers, start, end)]
    #     sorted_chunks = pool.starmap(sorting_two,items)
    # end2 = timer()
    # time2 = end2 - start2 


    # time_arr = []   
    # time_arr.append(time)
    # time_arr.append(time1)
    # time_arr.append(time2)
 
    # processes_arr = []
    # processes_arr .append(2)
    # processes_arr .append(4)
    # processes_arr .append(8)

    # plt.plot(processes_arr,time_arr)
    # plt.xlabel("Processes")
    # plt.ylabel("Time")
    # plt.show()

# if __name__ == '__main__':
#     sys.exit(main())
