from math import pi

class Cirkel:
    def __init__(self, x = 0, y = 0, r = 0):
        self.x = x
        self.y = y
        self.r = r

    def set_r(self, r):
        assert r >= 0
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def omkr(self):
        return 2 * pi * self.r

cirkel = Cirkel()
input = float(input("Ange cirkelns radie: "))

cirkel.set_r(input)

print("Area: ", cirkel.area())