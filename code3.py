def reverse_string(s):
    reversed_str=""  #initialize an empty string to store the reversed string
    l=len(s) 
    #iterate from the last character to the first
    for i in range(length-1,-1,-1):
        reversed_str+=s[i]  #appending each character to the reversed string
    return reversed_str

print(reverse_string("hello"))  
print(reverse_string("python"))  
