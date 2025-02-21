# 238. Product of Array Except Self
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''


def productExceptSelf(nums: list) -> list:
    n = len(nums)
    left_prod = [1] * (n + 1)
    right_prod = [1] * (n + 1)

    for i in range(n):
        left_prod[i] = left_prod[i-1] * nums[i]

    for i in range(n-1, -1, -1):
        right_prod[i] = right_prod[i+1] * nums[i]

    answer = []
    for i in range(n):
        answer.append(left_prod[i-1] * right_prod[i+1])
    
    return answer