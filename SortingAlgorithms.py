def insertion_sort(list):
    #The following is an implementation of the insertion sort algorithm.
    for i in range(1, len(list)):
        j = i
        while(j > 0 and list[j - 1] > list[j]):
            list[j], list[j-1] = list[j-1], list[j]
            j = j - 1
    return list

def selection_sort(list):
    #The following is an implementation of the selection sort algorithm.
    for i in range(0, len(list)):
        lowest = i
        for j in range(i, len(list)):
            if list[j] < list[lowest]:
                lowest = j
        list[i], list[lowest] = list[lowest], list[i]
    return list

def bubble_sort(list):
    #The following is an implementation of the bubble sort algorithm.
    while True:
        swapped = False
        for i in range(0, len(list)-1):
            if list[i] > list[i + 1]:
                swapped = True
                list[i], list[i + 1] = list[i + 1], list[i]
        if swapped == False:
            break
    return list

def merge_sort(list):
    # The following is an implementation of the merge sort algorithm.
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i + 1
            else:
                list[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return list

def partition(list,low,high):
    #Helper Function to be used with the provided implementation of quicksort.
    pivot = list[low]
    left = low + 1
    right = high
    boolean = False
    while(boolean == False):
        while(left <= right) and (list[left] <= pivot):
            left = left + 1
        while(right >= left) and (list[right] >= pivot):
            right = right - 1
        if left > right:
            boolean = True
        else:
            list[left], list[right] = list[right], list[left]
    list[low], list[right] = list[right], list[low]
    return right

def quick_sort_helper(list,low,high):
    #The following is an implementation of the quick-sort algorithm.
    if low < high:
        p = partition(list, low, high)
        quick_sort_helper(list, low, p-1)
        quick_sort_helper(list, p+1, high)

def quick_sort(list):
    #Function sorts and returns a list using the quick-sort algorithm above.
    #Uses helper functions and picks the first element as a pivot.
    quick_sort_helper(list, 0, len(list) - 1)
    return list

