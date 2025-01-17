def binary_search(arr, target):
    left, right = 0, len(arr) - 1  #initialize left and right pointers
    while left <= right:  #continue until the left pointer is less than or equal to the right pointer
        mid = left + (right - left) // 2  

        if arr[mid] == target: 
            return mid
        elif arr[mid] < target:  
            left = mid + 1  #left pointer to the right
        else:  
            right = mid - 1  # right pointer to the left

    return -1  


print(binary_search([1, 3, 5, 7, 9, 11], 5)) 
