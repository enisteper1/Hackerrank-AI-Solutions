def get_princess_loc(grid):
      y_loc = 0
      for i, row in enumerate(grid):
            if 'p' in row:
                  y_loc = i
                  break
      x_loc = row.index('p')
      return y_loc, x_loc

def nextMove(n,r,c,grid):

      # Get princess location
      y_loc, x_loc = get_princess_loc(grid)

      # Calculate vertical distance
      vertical_move = y_loc - r
      # move upward or downward if not on on same row
      if vertical_move > 0:
            return "DOWN"
      elif vertical_move < 0:
            return "UP"
      
      # Calculate horizontal distance
      horizontal_move = x_loc - c

      # move left or right if not on on same row
      if horizontal_move > 0:
            return "RIGHT"
      elif horizontal_move < 0:
            return "LEFT"
      return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))