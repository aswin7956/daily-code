def isPalindrome(s):
    new_str = ""
    for char in s:
        if char.isalpha(): #consider only characters
            new_str += char.lower() #standardize casing
    rev = "" 
    for i in range(len(new_str) - 1, -1, -1): #iterate in reverse
        rev += new_str[i] #concat and store reverse of the string
    return new_str == rev 
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))
