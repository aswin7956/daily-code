#Leetcode 1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        s = {}  #map to store index with val
        for i in range(len(nums)):  
            comp = target - nums[i]  #find the complement of target
            if comp in s.keys():  
                return [s[comp], i] # return indices when a match is found
            s[nums[i]] = i  
