from env import Env
from pipe import Pipe
from symbols import Symbols


class World:
    worldMap = None
    tick = 0

    def __init__(self):
        self.worldMap = [[Symbols.air for _ in range(Env.SCREEN_WIDTH)] for _ in range(Env.SCREEN_HEIGHT)]
        for i in range(len(self.worldMap[0])):
            self.worldMap[0][i] = self.worldMap[Env.SCREEN_HEIGHT - 1][i] = Symbols.wall

    def move(self):
        pipe = None
        if self.tick % 4 == 0:
            pipe = Pipe()

        for i in range(1, len(self.worldMap) - 1):
            for j in range(len(self.worldMap[i]) - 1):
                self.worldMap[i][j] = self.worldMap[i][j + 1]
            if pipe is None:
                self.worldMap[i][-1] = Symbols.air
            else:
                self.worldMap[i][-1] = pipe.structure[i]

        self.tick += 1

    def checkDeath(self, player):
        if self.worldMap[player.y][player.x] != Symbols.air:
            return True
        return False
