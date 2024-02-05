def get_max_sum_subarray(nums):
    max_sum, cur_sum = 0, float('-inf')
    start, end = 0, 0

    for idx in range(len(nums)):
        cur_sum += nums[idx]
        if cur_sum >= max_sum:
            max_sum = cur_sum
            end = idx
        if cur_sum <= 0:
            start = idx + 1
            cur_sum = 0
    
    return max_sum, start, end


