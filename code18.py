weight = int(input())  
waterlevel = input().upper()  # standardize to uppercase

if weight < 0:  
    print("Invalid weight")
elif weight == 0:  
    print("Time estimation is 0 minutes")
elif weight > 7000:  
    print("Weight overloaded")    #early return calls
else:
    time = 0  
    if waterlevel == 'L':  
        time = 25 if weight <= 2000 else 0 #25 if less than 2k
    elif waterlevel == 'M':  
        time = 35 if 2001 <= weight < 4000 else 0   #35 if btw 2k and 4k
    elif waterlevel == 'H': 
        time = 45 if 4000 <= weight < 7000 else 0  #45 if btw 4k and 7k
    else:
        print("Invalid water level")

    if time > 0:
        print(time)    #displaying the time taken
    else:
        print("Invalid value..")
