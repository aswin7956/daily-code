n = int(input())

#upper half
for i in range(1, n + 1):  # Loop from 1 to n
    for j in range(n - i, 0, -1):  #whitespacein reverse
        print(" ", end="")
    for k in range(2 * i - 1):  #odd number logic
        print("*", end="")
    print()  #next line

#lower half 
for i in range(n - 1, 0, -1):  #reverse logic
    for j in range(n - i):  
        print(" ", end="")
    for k in range(2 * i - 1, 0, -1):  
        print("*", end="")
    print()  # Move to the next line
