# https://www.hackerrank.com/challenges/botcleanr

def get_dirt_loc(board):
      y_loc = 0
      for i, row in enumerate(board):
            if 'd' in row:
                  y_loc = i
                  break
      x_loc = row.index('d')
      return y_loc, x_loc

def nextMove(posr, posc, board):
    y_loc, x_loc = get_dirt_loc(board)
    # Calculate vertical distance
    vertical_move = y_loc - posr
    # move upward or downward if not on on same row
    if vertical_move > 0:
        print("DOWN")
        return
    elif vertical_move < 0:
        print("UP")
        return
    # Calculate horizontal distance
    horizontal_move = x_loc - posc

    # move left or right if not on on same row
    if horizontal_move > 0:
        print("RIGHT")
        return
    elif horizontal_move < 0:
        print("LEFT")
        return
    
    print("CLEAN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)