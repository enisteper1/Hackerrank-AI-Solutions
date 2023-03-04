#!/usr/bin/python
def full_move(n,way):
    for i in range(n // 2):
       print(way)
       
def displayPathtoPrincess(n,grid):
  # if at top left 
  if grid[0][0] == 'p':
       full_move(n, 'UP')
       full_move(n, 'LEFT')
  # if at left bottom
  elif grid[n-1][0] == 'p':
        full_move(n, 'DOWN')
        full_move(n, 'LEFT')
  # if at right bottom
  elif grid[n-1][n-1] == 'p':
        full_move(n, 'DOWN')
        full_move(n, 'RIGHT')
  # if at right top      
  elif grid[0][n-1] == 'p':
        full_move(n, 'UP')
        full_move(n, 'RIGHT')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
