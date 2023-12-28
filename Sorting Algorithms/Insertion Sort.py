lst = [1, 4, 9, 10, -2, 3, 3, 0]

def bubble_sort(lst):
    sz = len(lst)

    for idx1 in range(1, sz):
        key = lst[idx1]
        idx2 = idx1 - 1

        while idx2 >= 0 and key < lst[idx2]:
            lst[idx2 + 1] = lst[idx2]
            idx2 -= 1
        lst[idx2 + 1] = key

    return lst

print(f"Before: {lst}\nAfter: {bubble_sort(lst)}")
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
