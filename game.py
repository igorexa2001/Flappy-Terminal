import threading
import time

import keyboard

from env import Env
from player import Player
from screen import Screen
from symbols import Symbols
from world import World


class Game:
    __screen = Screen()
    __world = World()
    __player = Player()

    __playerJumpHook = None
    __worldMoveThread = threading.Thread()
    __playerFallThread = threading.Thread()
    __playerJumpThread = threading.Thread()
    __displayThread = threading.Thread()

    isDead = False
    score = 0

    def __init__(self):
        self.__worldMoveThread = threading.Thread(target=self.__worldMove, daemon=True)
        self.__playerFallThread = threading.Thread(target=self.__playerFall, daemon=True)
        self.__displayThread = threading.Thread(target=self.__display, daemon=True)
        self.__playerJumpHook = keyboard.on_release_key(key='q', callback=self.__playerJump)

    def start(self):
        self.__worldMoveThread.start()
        self.__playerFallThread.start()
        self.__displayThread.start()
        self.__game()

    def __game(self):
        storedTick = None
        while (not keyboard.is_pressed('esc')) & (not self.isDead):
            if self.__world.checkDeath(self.__player):
                self.__death()
            if (self.__world.worldMap[1][self.__player.x] == Symbols.pipe) | (
                    self.__world.worldMap[Env.SCREEN_HEIGHT - 2][self.__player.x] == Symbols.pipe):
                if storedTick != self.__world.tick:
                    self.score += 1
                    storedTick = self.__world.tick

    def __death(self):
        self.isDead = True
        self.__screen.print(self.__world, self.__player, self.score)
        print('U died!')

    def __playerFall(self):
        while not self.isDead:
            time.sleep(0.5)
            self.__player.fall()

    def __playerJump(self, arg):
        if self.__player.y - 1 > 0:
            self.__player.jump()

    def __worldMove(self):
        while not self.isDead:
            time.sleep(0.7)
            self.__world.move()

    # TODO Improve print mechanism
    def __display(self):
        while not self.isDead:
            time.sleep(0.1)
            self.__screen.print(self.__world, self.__player, self.score)
