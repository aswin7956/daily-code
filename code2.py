
def is_prime(n):
    # SInce 1 isnt prime
    if n<=1:
        return False
    
    # Check from 2 to sqrt(n)
    for i in range(2,int(n**0.5)+1):
        #if divisible by any number it's not prime
        if n%i==0:
            return False
    return True

print(is_prime(29))  
print(is_prime(15))  

