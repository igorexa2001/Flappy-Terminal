import copy
import os

from symbols import Symbols


class Screen:
    def print(self, world, player, score):
        global screenMap
        screenMap = copy.deepcopy(world.worldMap)
        screenMap[player.y][player.x] = Symbols.player
        self.__clearScreen()
        for i in range(len(screenMap)):
            for j in range(len(screenMap[i])):
                print(screenMap[i][j], end=' ')
            print('')
        print('Score - ', score)

    @staticmethod
    def __clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')
