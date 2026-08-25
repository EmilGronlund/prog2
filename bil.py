class Person:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""
        self.födelseår = ""
        self.singel = True

class Bil:
    def __init__(self):
        self.ägare = None
        self.regnummer = ""
        self.fabrikat = ""
        self.årsmodell = ""
        self.tjänstevikt = ""
        self.motoreffekt = ""

b = Bil()
b.ägare = Person()
b.ägare.förnamn = "Bertil"

bil_1 = Bil()
bil_1.regnummer = "NDE384"
bil_1.fabrikat = "Volvo"
bil_1.årsmodell = "2015"
bil_1.tjänstevikt = "1650 kg"
bil_1.motoreffekt = "181 hk"

bil_2 = Bil()
bil_2.regnummer = "SJY467"
bil_2.fabrikat = "Audi"
bil_2.årsmodell = "2018"
bil_2.tjänstevikt = "1580 kg"
bil_2.motoreffekt = "150 hk"

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