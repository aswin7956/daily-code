class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:      # if both strings are true early return
            return True
        if len(s1) != len(s2):
            return False  # if len mismatch early return
        wrong_idx = [] # to store wrong index as a tuple
        for i in range(len(s1)): #  iterate over the length
            a=s1[i]  
            b=s2[i]
            if a != b:     # when mimatch found
                wrong_idx.append((a, b))  #append as tuple
                if len(wrong_idx) > 2: # if length exceeds 3 more than 2 mismatch found so return
                    return False
        if len(wrong_idx) != 2:   # if mismatch is only 1 then cannot swap so return
            return False
        c=wrong_idx[0]
        d=wrong_idx[1]
        return c == d[::-1] # check if 2nd element is reverse of first so that they can be swapped