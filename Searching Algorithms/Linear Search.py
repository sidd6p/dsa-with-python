lst = [1, 4, 9, 10, -2, 3, 0]


def linear_search(lst, element):
    for idx, value in enumerate(lst):
        if value == element:
            return idx

    return None


print(f"Before: {lst}\nAfter: {linear_search(lst, 10)}")
##################################################
# Time Complexity:
#   Worst Case: O(n),
#   Average Case: O(n)
#   Best Case: O(1)

# Space Complexity:
#   Worst Case: O(1)
#   Average Case: O(1)
#   Best Case: O(1)
##################################################


# ##################################################
# Linear search is not an efficient algorithm. That being said, we can use linear search in the following situations:
# When the list contains a small number of elements, such as 10, 50, or 100.
# When searching through an unsorted list. Unlike some other algorithms, linear search does not require the list to be sorted.
##################################################
