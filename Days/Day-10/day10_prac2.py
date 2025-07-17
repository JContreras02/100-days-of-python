def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year_input = int(input("Please enter a year: "))
print(is_leap_year(year_input))
