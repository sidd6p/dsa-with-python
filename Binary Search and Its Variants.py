"""
Binary Search and Its Variants (Iterative & Recursive)

| Algorithm                          | Best Case | Average Case | Worst Case |
|------------------------------------|-----------|--------------|------------|
| Binary Search (Iterative & Recursive) | O(1)      | O(log n)     | O(log n)   |
| First Occurrence (Iterative & Recursive) | O(1)      | O(log n)     | O(log n)   |
| Last Occurrence (Iterative & Recursive) | O(1)      | O(log n)     | O(log n)   |
"""


def binary_search_iterative(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def binary_search_recursive(nums, target, l, r):
    if l > r:
        return -1

    mid = l + (r - l) // 2

    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return binary_search_recursive(nums, target, mid + 1, r)
    else:
        return binary_search_recursive(nums, target, l, mid - 1)


def first_occurrence(nums, target):
    l, r = 0, len(nums) - 1
    sol = -1

    while l <= r:
        mid = l + (r - l) // 2
        if target == nums[mid]:
            r = mid - 1
            sol = mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return sol


def last_occurrence(nums, target):
    l, r = 0, len(nums) - 1
    sol = -1

    while l <= r:
        mid = l + (r - l) // 2
        if target == nums[mid]:
            l = mid + 1
            sol = mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return sol
