lst = [1, 4, 9, 10, -2, 3, 3, 0]


def merge(left, right):
    output = list()
    idx1, idx2 = 0, 0

    while idx1 < len(left) and idx2 < len(right):
        if left[idx1] < right[idx2]:
            output.append(left[idx1])
            idx1 += 1
        else:
            output.append(right[idx2])
            idx2 += 1
    
    output.extend(left[idx1:])
    output.extend(right[idx2:])

    return output

def merge_sort(lst):
    sz = len(lst)
    if sz <= 1: return lst

    mid = sz //2 

    left_partition = merge_sort(lst[:mid])
    right_partition = merge_sort(lst[mid:])
    

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
