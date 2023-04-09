# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate(self, nums):
    # brute force solution - using two loops and checking every numbers - O(n^2) - O(1)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] == nums[j]:
                return True
    return False

    # optimized solution - using set O(n) - O(n)

    return len(set(nums)) < len(nums)
