def perf_num(n):
    fact = 0
    for i in range(1, n):
        if n % i == 0:  
            fact += i
    return fact == n

num1 = 28
num2 = 7
print(perf_num(num1))  
print(perf_num(num2))  
