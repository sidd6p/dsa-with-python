lst = [1, 4, 9, 10, -2, 3, 3, 0]

def quick_sort(lst):
    sz = len(lst)

    if sz <= 1: return lst
    else:
        pivot = lst.pop(sz // 2)
        smallers, greaters = list(), list()

        for element in lst:
            if element > pivot:
                greaters.append(element)
            else:
                smallers.append(element)

    return quick_sort(smallers) + [pivot] + quick_sort(greaters)

print(f"Before: {lst}\nAfter: {quick_sort(lst)}")
##################################################
# Time Complexity:
#   Worst Case: O(n^2)
#   Average Case: O(n log n)
#   Best Case: O(n log n)

# Space Complexity:
#   Worst Case: O(n)
#   Average Case: O(log n)
#   Best Case: O(log n)
##################################################


# ##################################################
# When to use quick sort?
#   Use quick sort for quickly sorting large datasets. It's efficient and works best when dealing with diverse data.

# When not to use quick sort?
#   Avoid quick sort if you need a sorting algorithm that maintains the order of equal elements. Also, quick sort can be slow in worst-case scenarios.
#   Therefore, if worst-case time complexity is important, consider using merge sort instead.
##################################################
