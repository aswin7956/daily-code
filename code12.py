class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} #map for retrieval in constant time
        res=0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]: #when smaller char preceed bigger char reduce the sum
                res-=roman[s[i]]                             #edge case here is i+1 may go out of bounds so check and proceed
            else:
                res+=roman[s[i]] #when bigger char add the sum
            print(res)
        return res