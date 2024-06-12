class Board:
    def __init__(self):
        self.flipped = [1, 2, 3, 4]


class Game:
    def __init__(self):
        self.board = Board()

    def remove_last_flipped(self):
        last_flipped = self.board.flipped.pop()
        print("Removed element:", last_flipped)


game = Game()
game.remove_last_flipped()  # Виведе "Removed element: 4"
game.remove_last_flipped()  # Виведе "Removed element: 3"
