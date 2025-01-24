class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0 #left and reight pointers
        j=len(height)-1
        m=float("-inf") 
        while i<j:
            w=j-i
            h=min(height[i],height[j]) #in the bounds take min height
            area=h*w
            m=max(area,m)
            if height[i] < height[j]:
                i+=1    #move pointer from lower val to increment and find a better height 
            else:
                j-=1
        return m