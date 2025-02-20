# 217. Contains Duplicate
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

def containsDuplicate(self, nums: list) -> bool:
    unique = set()
    for num in nums:
        if num in unique:
            return True
        unique.add(num)
    return False