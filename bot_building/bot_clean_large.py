
import math

def get_closest_dirt_loc(posr, posc, board):
    y_loc = -1
    x_loc = -1
    dist = math.inf
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'd':
                calc_dist = abs(j - posc) + abs(i - posr)
                if calc_dist < dist:
                    dist = calc_dist
                    y_loc = i
                    x_loc = j

    return y_loc, x_loc

def next_move(posx, posy, dimx, dimy, board):
    y_loc, x_loc = get_closest_dirt_loc(posx, posy, board)

    # Calculate vertical distance
    vertical_move = y_loc - posx
    
    # Calculate horizontal distance
    horizontal_move = x_loc - posy
    
    # move upward or downward if not on on same row
    if vertical_move > 0:
        print("DOWN")
    elif vertical_move < 0:
        print("UP")

    # move left or right if not on on same row
    elif horizontal_move > 0:
        print("RIGHT")
    elif horizontal_move < 0:
        print("LEFT")
    else:
        print("CLEAN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)