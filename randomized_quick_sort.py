import random

def quicksort(a_list, left, right):
    if left < right:
        final_pivot_pos = rand_partition(a_list, left, right)
        quicksort(a_list, left, final_pivot_pos - 1)
        quicksort(a_list, final_pivot_pos + 1, right)

def rand_partition(a_list, left, right):
    rand = random.randrange(left, right)
    a_list[rand], a_list[right] = a_list[right], a_list[rand]
    return partition(a_list, left, right)

def partition(a_list, left, right):
    pivot = a_list[right]
    last_filled = left - 1
    for i in range(left, right):
        if a_list[i] <= pivot:
            last_filled = last_filled + 1
            a_list[last_filled], a_list[i] = a_list[i], a_list[last_filled]
    last_filled = last_filled + 1
    a_list[last_filled], a_list[right] = a_list[right], a_list[last_filled]
    return last_filled

def quicksort_helper(a_list):
    left = 0
    right = len(a_list) - 1
    quicksort(a_list, left, right)
    return a_list