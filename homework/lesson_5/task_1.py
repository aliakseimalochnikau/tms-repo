"""
Напишите функцию is_year_leap, которая принимает число (год) и возвращает True,
если год високосный, False - если нет.
"""


def is_year_leap(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


assert(is_year_leap(1700)) is False
assert(is_year_leap(2012)) is True
assert(is_year_leap(1904)) is True
assert(is_year_leap(1900)) is False
assert(is_year_leap(1600)) is True

