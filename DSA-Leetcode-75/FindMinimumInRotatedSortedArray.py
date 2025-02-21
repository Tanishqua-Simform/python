# 153. Find Minimum in Rotated Sorted Array
'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
'''

def findMin(nums: list) -> int:
    n = len(nums)
    l = 0
    r = n-1
    minimum = nums[0]
    while l < r:
        mid = (l + r) // 2
        minimum = min(minimum, nums[l], nums[r])
        if nums[l] <= nums[mid]:
            l = mid + 1
        elif nums[mid] <= nums[r]:
            r = mid
    return minimum