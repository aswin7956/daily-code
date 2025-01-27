import random
num1 = random.randint(1, 100)   #generate random 2 numbers
num2 = random.randint(1, 100)  
print(num1)
print(num2)
if num1 > num2:         #checking their relation
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")
