def fizzBuzz(n):
    arr = []
    for i in range(1, n + 1):  
        if i % 3 == 0 and i % 5 == 0: #can also be written as i % 15
            arr.append("FizzBuzz")
        elif i % 3 == 0: #only by 3
            arr.append("Fizz")
        elif i % 5 == 0: #only by 5
            arr.append("Buzz")
        else:
            arr.append(str(i)) #appending i as a string
    return arr
print(fizzBuzz(3))  
print(fizzBuzz(5))  
print(fizzBuzz(15))
