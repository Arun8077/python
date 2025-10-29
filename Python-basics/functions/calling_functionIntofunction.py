month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month > 12 or month < 1:  ##     if not 1 <= month <=12:
        return ('invalid month')
    if month == 2 and is_leap(True):
        return 29
    return month_days[month]

print(is_leap(2000))
print(days_in_month(2000, 2))
print(days_in_month(2000, 12))
print(days_in_month(2000, 14))

# $ python calling_functionIntofunction.py 
# True
# 29
# 31
# invalid month