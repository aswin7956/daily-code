class Solution(object):
    def maxAscendingSum(self, nums):
        t=0
        m=float("-inf")
        for i in range(len(nums)):
            if i==0:
                t+=nums[i]
            elif nums[i]>nums[i-1]:
                t+=nums[i]
            else:
                t=nums[i]
            m=max(m,t)
        return m

        