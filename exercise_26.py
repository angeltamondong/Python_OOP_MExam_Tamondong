class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def add_points(self, points):
        self.score += points
        return self.score


Anna = Player("Anna", 10)
Ben = Player("Ben")

print(Anna.add_points(5))
print(Ben.add_points(7))
