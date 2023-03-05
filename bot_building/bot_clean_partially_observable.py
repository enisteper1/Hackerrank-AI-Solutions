# https://www.hackerrank.com/challenges/botcleanv2

import math
import os

class GameBoard:
    def __init__(self, posx, posy, board):
        self._board = board
        self._posx = posx
        self._posy = posy
        self.board_filename = 'game_board.txt'

    def load_board(self):
        with open(self.board_filename, 'r') as f:
            board_str = f.read()
            board = []
            for row in board_str.split('\n'):
                board.append(row.split(','))
        return board
    
    def write_board(self, board):
        with open(self.board_filename, 'w') as f:
            board_str = ""
            for row in board:
                tmp = ",".join(row) + '\n'
                board_str += tmp
            f.write(board_str[:-1])

    # Update original board
    def update_board(self, posx, posy, board):
        if os.path.isfile(self.board_filename):
            self._board = self.load_board()
            self._posx = posx
            self._posy = posy
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != 'o':
                        self._board[i][j] = board[i][j]
        else:
            self.write_board(board)
            self._board = board
            self._posx = posx
            self._posy = posy
                    
    def check_target(self, posx, posy, target):
        row_loc = -1
        col_loc = -1
        max_dist = math.inf
        # Check for dirt
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                if self._board[i][j] == target:
                    calc_dist = abs(i - posx) + abs(j - posy)
                    # Get closest unobserved location
                    if calc_dist < max_dist:
                        max_dist = calc_dist
                        row_loc = i
                        col_loc = j

        return row_loc, col_loc
    
    def next_move(self, posx, posy, board):

        self.update_board(posx, posy, board)

        row_loc, col_loc = self.check_target(posx, posy, 'd')
        # Continue searching
        if row_loc == -1 and col_loc == -1:
            row_loc, col_loc = self.check_target(posx, posy, 'o')

        # Calculate vertical distance
        vertical_move = row_loc - posx
        
        # Calculate horizontal distance
        horizontal_move = col_loc - posy

        # move upward or downward if not on on same row
        if vertical_move > 0:
            print("DOWN")
        elif vertical_move < 0:
            print("UP")

        # move left or right if not on same row
        elif horizontal_move > 0:
            print("RIGHT")
        elif horizontal_move < 0:
            print("LEFT")
        else:
            print("CLEAN")

        self.write_board(self._board)
        
if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]
    gameboard = GameBoard(pos[0], pos[1], board)
    gameboard.next_move(pos[0], pos[1], board)