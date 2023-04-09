# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(self, nums, target):
    # brute force solution O(n^2) - O(1)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return i, j

    # optimized way
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return None
