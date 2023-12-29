lst = [-1, 0, 1, 1, 2, 5, 100, 282, 1111]


def binary_search(lst, element):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] > element:
            high = mid - 1
        elif lst[mid] < element:
            low = mid + 1
        else:
            return mid

    return None


print(f"{binary_search(lst, 11111)}")
##################################################
# Time Complexity:
#   Worst Case: O(log n)
#   Average Case: O(log n)
#   Best Case: O(1)

# Space Complexity:
#   Worst Case: O(1)
#   Average Case: O(1)
#   Best Case: O(1)
##################################################


# ##################################################
# Binary search is used in scenarios where the data is already sorted (or can be sorted easily). This includes:
#   Database search: Binary search can be used to quickly search through large databases to find specific records or elements.
#   Search Engines: Binary search can be used to locate a word or phrase in a sorted list of indexed terms.
##################################################
