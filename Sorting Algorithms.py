"""
Sorting Algorithms and Time Complexities

| Algorithm      | Best Case    | Average Case | Worst Case  |
|----------------|--------------|--------------|-------------|
| Bubble Sort    | O(n^2)       | O(n^2)       | O(n^2)      |
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


def merge(left, right):
    combined = list()
    i = j = 0
    l, r = len(left), len(right)

    while i < l and j < r:
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1

    if i < l:
        combined.extend(left[i:])
    if j < r:
        combined.extend(right[j:])

    return combined


def merge_sort(nums):
    n = len(nums)
    if n > 1:
        left = merge_sort(nums[: n // 2])
        right = merge_sort(nums[n // 2 :])
        return merge(left, right)
    return nums


def quick_sort(nums):
    n = len(nums)
    if n > 1:
        mid = nums[n // 2]
        left = [num for num in nums if num < mid]
        right = [num for num in nums if num > mid]
        mid = [num for num in nums if num == mid]
        return quick_sort(left) + mid + quick_sort(right)
    return nums
