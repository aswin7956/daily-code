# leetcode 15. 3Sum
class Solution(object):
    def threeSum(self, nums):  
        a = []  #initialize empty list
        nums.sort()  
        
        if nums[0] > 0:  
            return a  #early returning
        
        for i in range(len(nums)):  
            if i > 0 and nums[i] == nums[i - 1]:  #skip duplicate values 
                continue

            j = i + 1  
            k = len(nums) - 1  

            while j < k:  # Use two pointers to find pairs that sum to the negative of nums[i]
                s = nums[i] + nums[j] + nums[k]  #calculate the sum of the current triplet
                if s == 0: 
                    a.append([nums[i], nums[j], nums[k]])  #add the triplet to 'a' id the sum is found
                    j += 1  
                    while nums[j] == nums[j - 1] and j < k:  #skip duplicates 
                        j += 1
                elif s > 0:  # the sum is greater so decrement k to reduce s
                    k -= 1
                else: 
                    j += 1

        return a

a=Solution()
print(a.threeSum([-1,0,1,2,-1,-4])) # For local testing
