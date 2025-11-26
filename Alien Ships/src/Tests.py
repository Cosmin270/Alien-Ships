from Board import *
from BoardExceptions import *
import unittest



class Test(unittest.TestCase):
    def test_fire_1(self):
        board = Board()
        board.place_random_asteroids()
        board.place_random_ships()
        with self.assertRaises(InvalidFire):
            board.fire(3, 3)

    def test_fire_2(self):
        board = Board()
        board.place_random_asteroids()
        board.place_random_ships()
        bd = board.get_board()
        x = y = 0
        ok = False
        for i in range(7):
            for j in range(7):
                if bd[i][j] == " ":
                    x = i
                    y = j
                    ok = True
                    break
            if ok:
                break

        with self.assertRaises(CloseOne):
            board.fire(x, y)

    def test_fire_3(self):
        board = Board()
        board.place_random_asteroids()
        board.place_random_ships()
        bd = board.get_board()
        x = y = 0
        ok = False
        for i in range(7):
            for j in range(7):
                if bd[i][j] == "X":
                    x = i
                    y = j
                    ok = True
                    break
            if ok:
                break

        with self.assertRaises(NiceHitBro):
            board.fire(x, y)
if __name__ == '__main__':
    unittest.main()