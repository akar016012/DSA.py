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

    # more optimized way


def twoSum(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1


# My Documentation:
"""
# Approach
Two-pointer approach

# Complexity
- Time complexity:
Since, we are looping through the list once, the time complexity would be $$O(n)$$

- Space complexity:
Since, we are not using any extra space, the space complexity would be $$O(1)$$

# Code
```
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            #--Adding the numbers to get the total sum
            numSum = numbers[l] + numbers[r]
            #--If sum is less than the target move the left point up 
            if numSum < target:
                l+=1
            #--If sum is less than the target move the right point down 
            elif numSum > target:
                r-=1
            # If the sum equals the target return the two indexes
            else:
                return [l+1,r+1]
                    
```
"""
