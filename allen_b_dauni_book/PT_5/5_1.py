"""
import time
epoch_time = time.time()

seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_month = 30.4358
months_per_year = 12

seconds = epoch_time % seconds_per_minute
minutes = (epoch_time // seconds_per_minute) % minutes_per_hour
hours = (epoch_time // (seconds_per_minute * minutes_per_hour)) % hours_per_day
days = ((epoch_time // (seconds_per_minute * minutes_per_hour * hours_per_day)) % days_per_month) + 1
months = ((epoch_time // (seconds_per_minute * minutes_per_hour * hours_per_day * days_per_month)) % 12) + 1
years = (epoch_time // (seconds_per_minute * minutes_per_hour * hours_per_day * days_per_month * months_per_year)) + 1970
print(f'{years:.0f}-{months:.0f}-{days:.0f} {hours:.0f}:{minutes:.0f}:{seconds:.0f}')
"""
import time
epoch = time.time()

second = epoch % 60
minute = (epoch // 60) % 60
hour = (epoch // (60 * 60)) % 24
day = ((epoch // (60 * 60 * 24)) % 30.4358) + 1
month = (epoch // (60 * 60 * 24 * 30.4358)) % 12 + 1
year = (epoch // (60 * 60 * 24 * 30.4358 * 12)) + 1970
days_passed = epoch // (60 * 60 * 24)
match int(month):
    case 1:
        month = 'jan'
    case 2:
        month = 'feb'
    case 3:
        month = 'mar'
    case 4:
        month = 'apr'
    case 5:
        month = 'may'
    case 6:
        month = 'jun'
    case 7:
        month = 'jul'
    case 8:
        month = 'aug'
    case 9:
        month = 'sep'
    case 10:
        month = 'oct'
    case 11:
        month = 'nov'
    case 12:
        month = 'dec'
print('{}-{}-{} {}:{}:{}\nDays passed since epoch start: {}'.format(int(day), month, int(year), int(hour), int(minute), int(second), int(days_passed)), end='')