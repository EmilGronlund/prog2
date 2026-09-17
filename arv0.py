class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Admin(Player):
    def __init__(self, banCount, name, level):
        self.banCount = banCount
        super().__init__(name, level)

    def banPlayer(self, player):
        print(f"Player {player} was banned!")

p1 = Player("Steve", 23)
p2 = Admin(0, "Alex", 34689)

p2.banPlayer("Steve")