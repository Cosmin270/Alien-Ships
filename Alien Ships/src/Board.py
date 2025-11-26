from copy import deepcopy
from BoardExceptions import *
from texttable import Texttable
import string
import random



class Board:
    def __init__(self):
        self.__board = [[" " for _ in range(7)] for _ in range(7)]
        self.__board[3][3] = "E"
        self.__free_space = []
        for i in range(7):
            for j in range(7):
                if i != 3 and j != 3:
                    self.__free_space.append((i,j))
        self.__player_board = deepcopy(self.__board)
        self.__number_of_ships = 2

    def get_board(self):
        return self.__board
    def get_player_board(self):
        return self.__player_board

    def normal_matrix(self):
        table = Texttable()
        row = "/" + string.ascii_uppercase[:7]
        table.header(row)
        for i in range(7):
            row = f"{i+1}"
            for j in range(7):
                row += f"{self.__player_board[i][j]}"
            table.add_row(row)

        return table.draw()

    def cheat_matrix(self):
        table = Texttable()
        row = "/" + string.ascii_uppercase[:7]
        table.header(row)
        for i in range(7):
            row = f"{i + 1}"
            for j in range(7):
                row += f"{self.__board[i][j]}"
            table.add_row(row)

        return table.draw()

    def in_matrix(self, i, j):
        return i >= 0 and i <7 and j >= 0 and j <7

    def place_random_asteroids(self):
        cnt = 0
        while cnt < 8:
            place = random.choice(self.__free_space)
            x = place[0]
            y = place[1]
            ok = True
            for dx in -1, 0, 1:
                for dy in -1, 0, 1:
                    if self.in_matrix(x + dx, y + dy):
                        if self.__board[x+dx][y+dy] != " " or self.__board[x+dx][y+dy] == "E":
                            ok = False
            if ok:
                self.__board[x][y] = "*"
                self.__player_board[x][y] = "*"
                self.__free_space.remove(place)
                cnt += 1

    def place_random_ships(self):

        while True:
            x = random.randint(0, 6)
            y = random.choice([0, 6])
            if self.__board[x][y] == " ":
                self.__board[x][y] = "X"
                break
        while True:
            y = random.randint(0, 6)
            x = random.choice([0, 6])
            if self.__board[x][y] == " ":
                self.__board[x][y] = "X"
                break

    def fire(self, x, y):
        """
        It fires a cell into the board
        :param x: the row
        :param y: the column
        :return:
        It raises errors depending on the situation in order to catch them into UI and see the result:
            1. If it was in invalid move : InvalidFire error
            2. If it was a valid move, but you hit nothing : CloseOne error
            3. If it was a valid move and you hit a ship : NiceHitBro error
            4. If it was a valid move and you destroyed all ships : YouWon error
        """
        if self.__board[x][y] == "*" or self.__board[x][y] == '-' or self.__board[x][y] == "E":
            raise InvalidFire
        elif self.__board[x][y] == ' ':
            self.__board[x][y] = '-'
            self.__player_board[x][y] = '-'
            raise CloseOne
        elif self.__board[x][y] == "X":
            self.__board[x][y] = '-'
            self.__player_board[x][y] = '-'
            self.__number_of_ships -= 1
            if self.__number_of_ships:
                raise NiceHitBro
            else:
                raise YouWon
    def random_move_ship(self):
        rnd = []
        for i in range(0, 6):
            if self.__board[0][i] == ' ':
                rnd.append((0, i))
        for i in range(6, 0, -1):
            if self.__board[6][i] == ' ':
                rnd.append((6, i))
        for i in range(6, 0, -1):
            if self.__board[i][0] == ' ':
                rnd.append((i, 0))
        for i in range(6):
            if self.__board[i][6] == ' ':
                rnd.append((i, 6))

        for i in range(self.__number_of_ships+1):
            ok = False
            xi = yi = 0
            for j in range(7):
                for k in range(7):
                    if self.__board[j][k] == "X":
                        xi = j
                        yi = k
                        ok = True
                        break
                if ok:
                    break
            self.__board[xi][yi] = " "
            choice1 = random.choice([0,1])
            if not choice1:
                while True:
                    place = random.choice(rnd)
                    x = place[0]
                    y = place[1]
                    rnd.remove(place)
                    if self.__board[x][y] == " ":
                        self.__board[x][y] = "X"
                        break
            else:
                ok = False
                for j in range(7):
                    if self.__board[j][yi] == "E":
                        if j < xi:
                            self.__board[xi-1][yi] = "X"
                        else:
                            self.__board[xi+1][yi] = "X"
                        ok = True
                        break
                if not ok:
                    for j in range(7):
                        if self.__board[xi][j] == "E":
                            if j < yi:
                                self.__board[xi][yi-1] = "X"
                            else:
                                self.__board[xi][yi+1] = "X"
                            ok = True
                            break
                if not ok:
                    if xi > 3 and yi > 3:
                        self.__board[xi-1][yi-1] = "X"
                    elif xi > 3 and yi < 3:
                        self.__board[xi-1][yi+1] = "X"
                    elif xi < 3 and yi > 3:
                        self.__board[xi+1][yi-1] = "X"
                    else:
                        self.__board[xi+1][yi+1] = "X"
