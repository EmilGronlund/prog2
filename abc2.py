class Rektangel:
    def __init__(self, höjd, bredd):
        self.höjd = höjd
        self.bredd = bredd

    def area(self):
        return self.bredd * self.höjd

    def set_höjd(self, höjd):
        self.höjd = höjd

rektangel1 = Rektangel(3, 4)
rektangel1.set_höjd(7)

print(rektangel1.area())