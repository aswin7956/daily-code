def nambiar_number(n):
    n = str(n) # conversion to string 
    res = [] # list to store the intermediate strings or can use string too andjust concat result
    i = 0 
    l = len(n)
    while i < l: # loop till end
        cur = int(n[i])  
        j = i + 1 
        if cur % 2 == 1: # if odd  
            while j < l and cur % 2 != 0: #loop and add until sum is even
                cur += int(n[j])
                j += 1
        else:  
            while j < l and cur % 2 == 0: #if even loop and sum until sum is odd
                cur += int(n[j])
                j += 1
        res.append(str(cur))  
        i = j  # reset i to the new position from j as previous numbers were added
    return "".join(res) # join the list to display final res
N = 9962041247
print(nambiar_number(N))