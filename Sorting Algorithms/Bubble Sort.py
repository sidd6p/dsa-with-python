lst = [1, 4, 9, 10, -2, 3, 0]

def bubble_sort(lst):
    swapped = False
    sz = len(lst)

    for idx1 in range(sz - 1): # there will be no element to swap last element
        swapped = False
        for idx2 in range(sz - 1 - idx1): # after each outer loop, one element will be placed on right position from the end.
            if lst[idx2] > lst[idx2 + 1]:
                lst[idx2], lst[idx2 + 1] = lst[idx2 + 1], lst[idx2]
                swapped = True
        if not swapped:
            break
    
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

