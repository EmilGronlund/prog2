class Person:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""
        self.födelseår = ""
        self.singel = True

person1 = Person()
person1.förnamn = "Moa"
person1.efternamn = "Bergquist"
person1.födelseår = "2001"
person1.singel = True


print(person1.förnamn)