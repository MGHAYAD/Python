# Write a function that takes a year as input and determines if it's a leap year or not (a leap year is divisible by 4, except for years that are divisible by 100 but not by 400) 



def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False



year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")