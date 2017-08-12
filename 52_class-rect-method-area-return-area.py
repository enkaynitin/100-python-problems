class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

recA = Rectangle(3,4)
print recA.area()
