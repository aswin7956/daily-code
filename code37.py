def next_greater_element(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        next_greater = -1 # to store as -1 if no elemnt grater is found
        for j in range(i + 1, n): # from next element till end
            if arr[j] > arr[i]:
                next_greater = arr[j] #if greater found assign and break
                break
        result.append(next_greater)  #append values
    return result
arr = [1, 3, 2, 4]
print(next_greater_element(arr)) 
