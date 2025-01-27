def armstrong(n):
    num = str(n)  
    l = len(num)  
    s = 0 
    for i in num:  
        temp = int(i) ** l #number raised to the power of length
        s += temp   # add to temp
    if s == n:  
        return True
    else:
        return False
num = int(input())
if armstrong(num):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
