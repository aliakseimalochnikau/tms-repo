from my_time import MyTime


class MyTimeInterval:
    def __init__(self, start_seconds, finish_seconds):
        self.start = MyTime(start_seconds)
        self.finish = MyTime(finish_seconds)

    # Я переименовал метод для лучшего понимания того, что он делает
    def contains(self, my_time: MyTime):
        return self.start <= my_time <= self.finish

    def intersects(self, other: 'MyTimeInterval'):
        return self.start <= other.start <= self.finish or other.start <= self.start <= other.finish


if __name__ == '__main__':
    my_interval = MyTimeInterval(5, 50)
    assert my_interval.contains(MyTime(30))
    assert my_interval.contains(MyTime(5))
    assert my_interval.contains(MyTime(50))
    assert not my_interval.contains(MyTime(4))
    assert not my_interval.contains(MyTime(51))

    assert my_interval.intersects(MyTimeInterval(40, 61))
    assert my_interval.intersects(MyTimeInterval(5, 50))
    assert my_interval.intersects(MyTimeInterval(2, 15))
    assert my_interval.intersects(MyTimeInterval(50, 100))
    assert my_interval.intersects(MyTimeInterval(1, 5))
    assert my_interval.intersects(MyTimeInterval(20, 40))
    assert my_interval.intersects(MyTimeInterval(1, 60))
    assert not my_interval.intersects(MyTimeInterval(51, 70))
    assert not my_interval.intersects(MyTimeInterval(1, 4))






