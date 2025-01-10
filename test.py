def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def day_of_year_to_date(day, year):
    months_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap_year(year):
        months = months_leap
    else:
        months = months_normal
    
    month = 1
    while day > months[month - 1]:
        day -= months[month - 1]
        month += 1
    
    return f"{day:02}/{month:02}/{year}"

day,year = map(int,input().split())
print(day_of_year_to_date(day, year))
