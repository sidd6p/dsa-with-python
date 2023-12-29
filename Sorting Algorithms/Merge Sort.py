lst = [1, 4, 9, 10, -2, 3, 3, 0]


def merge(left, right):
    """
    Merges two sorted lists (left and right) into one sorted list.

    The function iterates over both lists, comparing their elements one by one.
    The smaller element from either list is appended to the output list.
    This process continues until all elements from both lists are included in the output list.
    """
    # Merges two sorted lists into one sorted list.
    output = list()
    idx1, idx2 = 0, 0

    # Iterate through both lists, comparing elements and adding the smaller one to the output.
    while idx1 < len(left) and idx2 < len(right):
        if left[idx1] < right[idx2]:
            output.append(left[idx1])
            idx1 += 1  # Move forward in the left list
        else:
            output.append(right[idx2])
            idx2 += 1  # Move forward in the right list

    # Extend the output with any remaining elements in left and right lists.
    output.extend(left[idx1:])
    output.extend(right[idx2:])

    return output


def merge_sort(lst):
    """
    This function divides the list into two halves, recursively sorts each half,
    and then merges the sorted halves back together. The base case for the recursion
    is when the size of the list is 1 or 0, at which point the list is already sorted.
    """
    # Recursively sorts a list using the merge sort algorithm.
    sz = len(lst)
    if sz <= 1:
        return lst  # Base case: A list of size 1 or less is already sorted

    mid = sz // 2

    # Divide the list into two halves and recursively sort each half.
    left_partition = merge_sort(lst[:mid])
    right_partition = merge_sort(lst[mid:])

    # Merge the two sorted halves.
    return merge(left_partition, right_partition)


print(f"Before: {lst}\nAfter: {merge_sort(lst)}")
##################################################
# Time Complexity:
#   Worst Case: O(n log n)
#   Average Case: O(n log n)
#   Best Case: O(n log n)

# Space Complexity:
#   Worst Case: O(n)
#   Average Case: O(n)
#   Best Case: O(n)
##################################################


# ##################################################
# Applications of Merge Sort
#   Use merge sort to sort large amounts of data accurately and efficiently.
#   It works better than bubble sort, slection sort and insertion sort in most cases.
##################################################
