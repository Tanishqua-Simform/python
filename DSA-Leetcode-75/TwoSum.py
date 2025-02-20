# 1. Two Sum -
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def twoSum(self, nums: list, target: int) -> list:
    visited = dict()
    for i, num in enumerate(nums):
        diff = target - num
        if diff in visited:
            return [i, visited[diff]]
        else:
            visited[num] = i