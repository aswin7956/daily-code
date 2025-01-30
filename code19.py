def check_anagram(s1, s2):
    if len(s1) != len(s2):  # early return if unequal lengths
        return False
    hshmp = {} #map to store key : value , here char:count
    for c in s1:
        if c not in hshmp.keys(): # if new char initialize to 1
            hshmp[c]=1
            continue
        hshmp[c] +=1
    for c in s2:
        if c not in hshmp.keys() or hshmp[c] == 0: #if key doesnt exist or count is 0
            return False
        hshmp[c] -=1 #negate the values in dict 
    return True
s1 = input()
s2 = input()
print(check_anagram(s1, s2))
