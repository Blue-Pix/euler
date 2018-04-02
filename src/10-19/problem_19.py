# -*- coding: utf-8 -*-

''' Problem 19
You are given the following information, but you may prefer to do some research for yourself.

・1 Jan 1900 was a Monday.
・Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
・A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

20世紀に日曜日から始まる月はいくつあったか
'''


def get_days_of_month(year, month):
    if month == 2:
        if year % 400 != 0 and year % 4 == 0:
            return 29
        return 28
    elif month in {9, 4, 6, 11}:
        return 30
    else:
        return 31


if __name__ == '__main__':
    total_days = 1
    sum_of_sundays = 0

    for year in range(1901, 2000):
        for month in range(1, 13):
            # begins with Sunday
            if total_days % 7 == 0:
                sum_of_sundays += 1

            # this month has
            days = get_days_of_month(year, month)
            total_days += days

    print('%d Sundays fell on the first of the month during the 20th century.' % sum_of_sundays)
