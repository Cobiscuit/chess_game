import pygame

# here ill be making the functions to see if the player wants to play against another player or AI... not sure how
#ill impliment AI yet... but well get there!


class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_move(self, move):
        pass




class HumanPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)
        print(f"{self.name} moves: {move}")

class AIPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)
        print(f"{self.name} moves: {move}")

