def singleNumber(nums):
    hshset = set()
    for i in nums:
        if i in hshset:
            hshset.remove(i)  # remove if in set
        else:
            hshset.add(i)  # add to set if not in set
    return hshset.pop()  # return last single element in the set
nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
print(singleNumber(nums1))  
print(singleNumber(nums2)) 
