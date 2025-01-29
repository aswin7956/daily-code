def subs(s):
    for i in range(len(s)):
        st = '' 
        for j in range(i, len(s)):     #for substrings
            st += s[j]             
            print(st)  
s = "sak"
subs(s)

