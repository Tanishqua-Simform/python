# 152. Maximum Product Subarray
'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
'''

def maxProduct(nums: list) -> int:
    max_product = max(nums)
    max_sub = 1
    min_sub = 1

    for n in nums:
        prod_1 = max_sub * n
        prod_2 = min_sub * n
        max_sub, min_sub = max(prod_1, prod_2, n), min(prod_1, prod_2, n)
        max_product = max(max_product, max_sub)
    return max_product