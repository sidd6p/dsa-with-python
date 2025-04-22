"""
Sorting Algorithms and Time Complexities

| Algorithm      | Best Case    | Average Case | Worst Case  |
|----------------|--------------|--------------|-------------|
| Bubble Sort    | O(n)         | O(n^2)       | O(n^2)      |
| Insertion Sort | O(n)         | O(n^2)       | O(n^2)      |
| Selection Sort | O(n^2)       | O(n^2)       | O(n^2)      |
| Merge Sort     | O(n log n)   | O(n log n)   | O(n log n)  |
| Quick Sort     | O(n log n)   | O(n log n)   | O(n^2)      |
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums

# Merge Sort
def merge_sort(arr):
    """Sorts an array using Merge Sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)
    return arr  # Time Complexity: O(n log n) in all cases


def merge(left, right):
    """Merges two sorted halves."""
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


# Quick Sort
def quick_sort(arr):
    """Sorts an array using Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    # Time Complexity: O(n log n) average, O(n^2) worst (bad pivot selection)
