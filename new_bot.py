import random

class NewBot:
    def __init__(self) -> None:
        self.dynamite = 100
        self.opDynamite = 0
        self.points = 1
        self.threshold = 3

    def make_move(self, gameState):
        #How much dynamite has our opponent used?
        if gameState['rounds']:
            if gameState['rounds'][-1]['p2'] == 'D':
                self.opDynamite += 1
            if gameState['rounds'][-1]['p1'] == gameState['rounds'][-1]['p2']:
                self.points += 1
            else:
                self.points = 1

        if self.points >= self.threshold and self.dynamite > 0:
            choice = 'D'
        else:
            choice = random.choice(['R', 'P', 'S'])
        
        if choice == 'D':
            self.dynamite -= 1
        return choice
