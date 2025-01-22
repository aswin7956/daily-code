class Solution:
    def isPalindrome(self, x) :
        if x<0: 
            return False #negative numbers not palindrome due to the - dign
        rev=0
        temp=x
        while temp!=0:
            digit=temp%10 #extract last digit
            rev = rev * 10 + digit
            temp//=10 #remove the digit
        return rev == x