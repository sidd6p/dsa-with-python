lst = [1, 4, 9, 10, -2, 3, 0]


def bubble_sort(lst):
    """
    Sorts a list of elements using the bubble sort algorithm.

    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    """

    # Flag to track if a swap was made in the current pass.
    swapped = False

    # Get the number of elements in the list.
    sz = len(lst)

    # Outer loop goes over each element in the list.
    for idx1 in range(sz - 1):  # No need to compare the last element in the final pass.
        # Reset swapped flag for the current pass.
        swapped = False

        # Inner loop for comparing adjacent elements.
        # As the list gets sorted, the last 'idx1' elements are already in place,
        # so the inner loop can avoid comparing them.
        for idx2 in range(sz - 1 - idx1):
            # Compare and swap if elements are in the wrong order.
            if lst[idx2] > lst[idx2 + 1]:
                lst[idx2], lst[idx2 + 1] = lst[idx2 + 1], lst[idx2]
                swapped = True

        # If no two elements were swapped in the inner loop, the list is sorted.
        if not swapped:
            break

    # Return the sorted list.
    return lst


print(f"Before: {lst}\nAfter: {bubble_sort(lst)}")
##################################################
# Time Complexity:
#   Worst Case: O(n^2), the list is in reverse order
#   Average Case: O(n^2)
#   Best Case: O(n), the list is already sorted

# Space Complexity:
#   Worst Case: O(1) becuase it is in-place sorting
#   Average Case: O(1) becuase it is in-place sorting
#   Best Case: O(1) becuase it is in-place sorting
##################################################


# ##################################################
# When to use bubble sort?
# Small datasets.
# When simplicity is more important than efficiency.
# When the data is already partially sorted.

# When not to use bubble sort?
# Avoid bubble sort for large datasets and performance-critical applications.
# In such cases, sorting algorithms like merge sort or quick sort are more suitable.
##################################################
