lst = [1, 4, 9, 10, -2, 3, 3, 0]


def quick_sort(lst):
    """
    Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element
    from the array and partitioning the other elements into two sub-arrays, according to whether
    they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

    """

    # Base case: lists with 0 or 1 elements are already sorted
    sz = len(lst)
    if sz <= 1:
        return lst
    else:
        # Selecting the pivot element from the middle of the list
        pivot = lst.pop(sz // 2)
        smallers, greaters = list(), list()

        # Dividing elements into those smaller than the pivot and those greater
        for element in lst:
            if element > pivot:
                greaters.append(element)
            else:
                smallers.append(element)

        # Recursively applying quick_sort on the smaller elements, the pivot, and the greater elements
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
