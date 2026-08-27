class Person:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""
        self.födelseår = ""
        self.singel = True

class Bil:
    def __init__(self, ägare=None, regnummer="", fabrikat="", årsmodell="", tjänstevikt="", motoreffekt=""):
        self.ägare = ägare
        self.regnummer = regnummer
        self.fabrikat = fabrikat
        self.årsmodell = årsmodell
        self.tjänstevikt = tjänstevikt
        self.motoreffekt = motoreffekt

bil_1 = Bil(Person(), "NDE384", "Volvo", "2015", "1650 kg", "181 hk")

bil_2 = Bil(Person(), "SJY467", "Audi", "2018", "1580 kg", "150 hk")

print(bil_1.regnummer)
print(bil_1.fabrikat)
print(bil_1.årsmodell)
print(bil_1.tjänstevikt)
print(bil_1.motoreffekt)
print()
print(bil_2.regnummer)
print(bil_2.fabrikat)
print(bil_2.årsmodell)
print(bil_2.tjänstevikt)
print(bil_2.motoreffekt)