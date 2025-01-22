class Solution:
    def reverse(self, x: int) -> int:
        a=abs(x) #convert to positive val for reversal, if we perform with negative number it would end up in an inf loop
        b=0
        while(a!=0):
            rem=a%10 #extract digit
            b=b*10+rem
            a=a//10 #remove the digit
        if b>2**31-1: #edge case
            return 0
        if(x<0): #to handle negative input so it will apply after the reversal
            b=-b
        return b