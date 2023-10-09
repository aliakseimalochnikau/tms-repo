class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)
p_a = Point(-5, -3)
p_b = Point(-2, -8)


print('Distance between p1 and zero point:', p1.distance_to_zero())
print('Distance between p2 and zero point:', p2.distance_to_zero())
print('Distance between p3 and zero point:', p3.distance_to_zero())
print('Distance between p_a and zero point:', p_a.distance_to_zero())
print('Distance between p_b and zero point:', p_b.distance_to_zero())
print('Distance between p1 and p1:', p1.distance_to_point(p1))
print('Distance between p1 and p2:', p1.distance_to_point(p2))
print('Distance between p2 and p1:', p2.distance_to_point(p1))
print('Distance between p1 and p3:', p1.distance_to_point(p3))
print('Distance between p2 and p3:', p2.distance_to_point(p3))
print('Distance between p_a and p_b:', p_a.distance_to_point(p_b))