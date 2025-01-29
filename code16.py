def func1(s):
    l = 0
    r = len(s) - 1
    
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True

str1 = input()
if func1(str1):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
