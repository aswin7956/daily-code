def dayOfYear(date):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_parts = date.split('-')
    year = int(date_parts[0]) 
    month = int(date_parts[1]) 
    day = int(date_parts[2])  
    def leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True  #by 400  it's a leap year
                else:
                    return False  #by 100 but not by 400 not a leap year
            else:
                return True  #by 4 but not by 100
        else:
            return False  #not a leap year
    if leap(year):
        days[1] = 29  
    res = 0
    for i in range(month - 1):  # Loop through the months before the given month
        res += days[i]  # Add the days in the previous months
    res += day
    return res
print(dayOfYear("2019-01-09"))  
print(dayOfYear("2019-02-10"))  
print(dayOfYear("2020-02-29"))  
