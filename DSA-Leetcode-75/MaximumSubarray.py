# 53. Maximum Subarray
'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

def maxSubArray(nums: list) -> int:
    curr_sum = 0
    max_sum = nums[-1]
    for n in nums:
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum