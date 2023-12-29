lst = [1, 4, 9, 10, 2, 3, 3, 0]

def counting_sort(lst):
    max_element = max(lst)
    counting_lst, sorted_lst =  [0] * (max_element + 1), list() 

    for element in lst:
        counting_lst[element] += 1

    for idx, count in enumerate(counting_lst):
        sorted_lst.extend([idx] * count)
        
    # for idx in range(len(counting_lst) - 1, -1, -1):
    #     sorted_lst.extend([idx] * counting_lst[idx])

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
