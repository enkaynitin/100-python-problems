
class Circle(object):
    def __init__(self, r):
        self.radius = r


    def area(self):
        return self.radius**2*3.14

acir = Circle(2)
print acir.area()
