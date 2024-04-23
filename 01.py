class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        self.radius = radius
        self.all_circles.append(self.radius)

    def area(self):
        area_of_circle = Circle.pi * self.radius ** 2
        return area_of_circle

    def __str__(self):
        return f'{self.radius}'

    def __len__(self):
        return len(self.all_circles)

    @staticmethod
    def total_area():
        total = 0
        for radius in Circle.all_circles:
            total += Circle.pi * radius**2
        return total


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c1)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
