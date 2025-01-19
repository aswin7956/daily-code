class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0 #initailizing pointers for taversal
        while i < n or j < m: 
           # print(i, j)
           # print(nums1)
            if j >= len(nums2): #to avoid Indexoutofbounds when j is exhausted
                break
            if i >= len(nums1):
                nums1.append(nums2[j]) #when i is exhauseted append all remaining elemts of nums2
                j+=1
                continue
            if nums1[i] < nums2[j]:
                i += 1 
                continue  
            else:
                nums1.insert(i, nums2[j]) # inserting the element in its sorted position
                j += 1
                continue
      #  print("while over")
       # print(nums1)
        if (len(nums1)%2) == 0:
            return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2 #median logic for even elements
        else:
            return nums1[len(nums1)//2] # odd elements