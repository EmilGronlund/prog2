class Person:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""
        self.födelseår = ""
        self.singel = True

class Bankkonto:
    def __init__(self):
        self.kontohavare = None
        self.saldo = 0

k = Bankkonto()
k.kontohavare = Person()
k.kontohavare.förnamn = "Bertil"