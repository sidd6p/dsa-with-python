lst = [1, 4, 9, 10, 2, 3, 3, 0]


def counting_sort(lst):
    """
    Counting sort is an efficient sorting algorithm that operates by counting the number of occurrences of each unique element in the input list. Then, it calculates the position of each element in the sorted array.

    Steps:
    1. Find the maximum element in the input list to determine the range of values.
    2. Initialize a counting list (array) with a length of max_element + 1, all set to 0.
    3. Count each element in the input list and increment the corresponding index in the counting list.
    4. Construct the sorted list by appending each element according to its count in the counting list.

    Note:
    - This implementation assumes that the input list contains only non-negative integers.
    """

    # Find the maximum element to determine the size of the counting array
    max_element = max(lst)

    # Initialize a counting array to store the frequency of each element
    # and an empty list for the sorted elements
    counting_lst, sorted_lst = [0] * (max_element + 1), list()

    # Count the occurrences of each element in the input list
    for element in lst:
        counting_lst[element] += 1

    # Construct the sorted list using the counts from the counting array
    for idx, count in enumerate(counting_lst):
        # Extend the sorted list with 'count' number of occurrences of 'idx'
        sorted_lst.extend([idx] * count)

    return sorted_lst


print(f"Before: {lst}\nAfter: {counting_sort(lst)}")
##################################################
# Time Complexity:
#   Worst Case: O(n + max)
#   Average Case: O(n + max)
#   Best Case: O(n + max)

# Space Complexity:
#   Worst Case: O(max)
#   Average Case: O(max)
#   Best Case: O(max)
##################################################


# ##################################################
# When to use counting sort?
#   Counting sort is highly efficient for sorting non-negative integers within a limited range.

# When not to use counting sort?
#   Avoid using counting sort when dealing with a wide range of values or when you have negative integers.
#   In such cases, other sorting algorithms such as quick sort or merge sort are preferable.
##################################################
