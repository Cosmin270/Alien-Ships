from Board import *
from copy import deepcopy
from BoardExceptions import *
from texttable import Texttable
import string
import random

class UI:
    def __init__(self, board : Board):
        self.__board = board
        self.__user_turn = True
    def prin_menu(self):
        print("What do you want to do?")
        print("1. fire (Eg. fire B2) ")
        print("2. cheat (-aura points, don't be a cheater)")

    def start(self):
        self.__board.place_random_asteroids()
        self.__board.place_random_ships()

        print("Your initial board is this: ")
        print(self.__board.normal_matrix())
        while True:

            self.prin_menu()
            option = input(">")

            if option[0] == 'f':
                opt, coord = option.split(" ")
                x = int(coord[1])-1
                dict = {"A": 0, "B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
                y = dict[coord[0]]
                try:
                    self.__board.fire(x, y)
                except InvalidFire as IF:
                    print(IF)
                except CloseOne as co:
                    print(self.__board.normal_matrix())
                    print(co)
                except NiceHitBro as nhb:
                    print(self.__board.normal_matrix())
                    print(nhb)
                except YouWon as yw:
                    print(self.__board.normal_matrix())
                    print(yw)
                self.__board.random_move_ship()
            else:
                print("Neah you are a cheater bro. This is the board:")
                print(self.__board.cheat_matrix())

board = Board()
ui = UI(board)
ui.start()