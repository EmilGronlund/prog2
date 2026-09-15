class Bil:
    def __init__(self, regnummer, märke, hastighet):
        self.__regnummer = regnummer
        self.märke = märke
        self.hastighet = hastighet

    def get_regnummer(self):
        return self.__regnummer

    def set_regnummer(self, nyRegnummer):
        self.__regnummer = nyRegnummer

bil = Bil("A7HBU4", "Audi", "150 km/h")

bil.set_regnummer("ABC123")

print(bil.get_regnummer())
print(bil.märke)
print(bil.hastighet)