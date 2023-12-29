lst = [1, 4, 9, 10, -2, 3, 3, 0]


def insertion_sort(lst):
    """
    Perform an insertion sort on a list.

    This function sorts a list in ascending order using the insertion sort algorithm.
    The algorithm builds the sorted list one element at a time by repeatedly taking
    the next unsorted element and inserting it into the correct position.
    """

    # Get the size of the list
    sz = len(lst)

    # Iterate over each element in the list starting from the second element
    for idx1 in range(1, sz):
        key = lst[idx1]  # The element to be inserted
        idx2 = idx1 - 1  # Start comparing with the element just before idx1

        # Shift elements of lst[0..idx1-1] that are greater than key
        # to one position ahead of their current position
        while idx2 >= 0 and key < lst[idx2]:
            lst[idx2 + 1] = lst[idx2]
            idx2 -= 1

        # Insert the key at after the element just smaller than it
        lst[idx2 + 1] = key

    return lst


print(f"Before: {lst}\nAfter: {insertion_sort(lst)}")
##################################################
# Time Complexity:
#   Worst Case: O(n^2)
#   Average Case: O(n^2)
#   Best Case: O(n)

# Space Complexity:
#   Worst Case: O(1)
#   Average Case: O(1)
#   Best Case: O(1)
##################################################


# ##################################################
# When to use insertion sort?
#   Use insertion sort for small lists or when your data is mostly in order. It's simple and works well when dealing with a limited number of items.

# When not to use insertion sort?
#   Avoid insertion sort for larger lists or when speed is essential. It can become slow for bigger datasets.
#   In those cases, opt for faster algorithms like merge sort or quick sort for better performance.
##################################################
