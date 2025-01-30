def perf_num(n):
    fact = 0
    for i in range(1, n): #iterate from 1 to num
        if n % i == 0:  
            fact += i #add the divisor
    return fact == n #return bool

num1 = 28
num2 = 7
print(perf_num(num1))  
print(perf_num(num2))  
