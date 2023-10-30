class MyTime:
    def __init__(self, seconds: float):
        self.seconds = seconds

    @property
    def hours(self):
        return int(self.seconds // 3600)

    @property
    def minutes(self):
        return int(self.seconds // 60)

    def __mul__(self, num):
        return MyTime(self.seconds * num)

    def __truediv__(self, num):
        return MyTime(self.seconds / num)

    def __add__(self, other):
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other):
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self):
        return f'{self.hours:02d}:{self.minutes % 60:02d}:{self.seconds % 60:04.1f}'

    def __str__(self):
        return f'{self.seconds}s'

    def __gt__(self, other):
        return self.seconds > other.seconds

    def __lt__(self, other):
        return self.seconds < other.seconds

    def __ge__(self, other):
        return self.seconds >= other.seconds

    def __le__(self, other):
        return self.seconds <= other.seconds

    def __eq__(self, other):
        return self.seconds == other.seconds

    def __ne__(self, other):
        return self.seconds != other.seconds


if __name__ == '__main__':

    assert MyTime(3720).hours == 1
    assert MyTime(3720).minutes == 62
    assert MyTime(10) * 2 == MyTime(20)
    assert MyTime(10) / 2 == MyTime(5)
    assert MyTime(10) + MyTime(5) == MyTime(15)
    assert MyTime(20) - MyTime(10) == MyTime(10)
    assert MyTime(3724.5).get_formatted_str() == '01:02:04.5'
    assert str(MyTime(2480)) == '2480s'
    assert MyTime(5) > MyTime(2)
    assert MyTime(5) >= MyTime(3)
    assert MyTime(5) >= MyTime(5)
    assert MyTime(6) < MyTime(10)
    assert MyTime(3) <= MyTime(10)
    assert MyTime(10) <= MyTime(10)
    assert MyTime(5) == MyTime(5)
    assert MyTime(5) != MyTime(10)

