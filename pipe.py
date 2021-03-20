import random

from env import Env
from symbols import Symbols


class Pipe:
    structure = None

    def __init__(self):
        self.structure = [Symbols.pipe for j in range(Env.SCREEN_HEIGHT)]
        holeHeight = random.randint(4, Env.SCREEN_HEIGHT - 4)
        pipeHole = [holeHeight - 1, holeHeight, holeHeight + 1]
        for i in pipeHole:
            self.structure[i] = Symbols.air
