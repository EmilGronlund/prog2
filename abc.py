class Player:
    def __init__(self, level, HP):
        self.level = level
        self.HP = HP

    def levelUp(self, amount):
        self.level += amount

    def takeDamage(self, amount):
        self.HP -= amount

    def attack(self):
        print("Player attacks!")

player1 = Player(10, 100)
player1.levelUp(5)
player1.takeDamage(50)

print(player1.level)
print(player1.HP)