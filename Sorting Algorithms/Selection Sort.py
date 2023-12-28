lst = [1, 4, 9, 10, -2, 3, 0]

def selection_sort(lst):
    sz = len(lst)
    total_swaps = 0

    for idx1 in range(sz - 1):
        cur_idx = idx1
        for idx2 in range(idx1 + 1, sz):
            if lst[cur_idx] > lst[idx2]:
                cur_idx = idx2  
        if cur_idx != idx1:
            total_swaps += 1
            lst[cur_idx], lst[idx1] = lst[idx1], lst[cur_idx]
    
    print(f"Total swaps made: {total_swaps}")
    return lst

print(f"Before: {lst}\nAfter: {selection_sort(lst)}")

##################################################
# Time Complexity:
#   Worst Case: O(n^2)
#   Average Case: O(n^2)
#   Best Case: O(n^2)

# Space Complexity:
#   Worst Case: O(1)
#   Average Case: O(1)
#   Best Case: O(1)
##################################################


# ##################################################
# When to use selection sort?
#   Use selection sort for small lists where simplicity is more important than speed.
#   While this also applies to bubble sort, selection sort generally requires fewer swaps. Therefore, it's favored over bubble sort when the cost of swapping significantly outweighs the cost of comparisons.

# When not to use selection sort?
#   Avoid selection sort for larger lists or situations where speed is crucial.
#   Merge sort and quick sort are preferable for larger lists.
##################################################
