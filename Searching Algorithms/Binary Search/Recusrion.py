lst = [-1, 0, 1, 1, 2, 5, 100, 282, 1111]


def binary_search(lst, low, high, element):
    if low <= high:
        mid = low + (high - low) // 2
        if lst[mid] > element:
            return binary_search(lst, low, mid - 1, element)
        elif lst[mid] < element:
            return binary_search(lst, mid + 1, high, element)
        else:
            return mid

    return None


print(f"{binary_search(lst ,0, len(lst) - 1, 5)}")
##################################################
# Time Complexity:
#   Worst Case: O(log n)
#   Average Case: O(log n)
#   Best Case: O(1)

# Space Complexity:
#   Worst Case: O(log n)
#   Average Case: O(log n)
#   Best Case: O(log n)
##################################################
