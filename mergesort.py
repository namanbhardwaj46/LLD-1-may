from concurrent.futures.thread import ThreadPoolExecutor
import time
import random
from concurrent.futures.process import ProcessPoolExecutor



def mergesort(leftarr, rightarr):
    result = []
    left = 0
    right = 0

    while left < len(leftarr) and right < len(rightarr):
        if leftarr[left] <= rightarr[right]:
            result.append(leftarr[left])
            left += 1
        else:
            result.append(rightarr[right])
            right += 1

    result.extend(leftarr[left:])
    result.extend(rightarr[right:])
    return result


def parllel_merge_sort(arr, worker):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    if len(arr)<1000 or worker <1 :
        left_sorted = parllel_merge_sort(left, worker)
        right_sorted = parllel_merge_sort(right, worker)
        return mergesort(left_sorted, right_sorted)

    with ProcessPoolExecutor(max_workers=worker) as executor:
        left_future = executor.submit(parllel_merge_sort, left, worker//2)
        right_future = executor.submit(parllel_merge_sort, right, worker//2)

        left_arr = left_future.result()
        right_arr = right_future.result()

        return mergesort(left_arr, right_arr)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return mergesort(left_sorted, right_sorted)

if __name__ =="__main__":
    arr = [random.randint(0,100) for i in range(5000000)]

    workers = 3

    t1 = time.time()


    val = merge_sort(arr.copy())

    t2 = time.time()

    print("Merge sort time:", t2-t1)


    t1 = time.time()
    sorted_arr = parllel_merge_sort(arr, workers)
    t2 = time.time()

    print(f"Execution time {t2-t1}")

