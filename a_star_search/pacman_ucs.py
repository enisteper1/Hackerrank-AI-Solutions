# https://www.hackerrank.com/challenges/pacman-ucs

class PacMan:
    
    def __init__(self, **kwargs):
        # Define pacman position
        self.pac_pos_r = kwargs.get('pac_pos_r')
        self.pac_pos_c = kwargs.get('pac_pos_c')
        # Define food position
        self.food_pos_r = kwargs.get('food_pos_r')
        self.food_pos_c = kwargs.get('food_pos_c')
        # Define grid
        self.grid = kwargs.get('grid')
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        # Placeholder to check is visited
        self.visited = list()
        # Placeholder to explored
        self.explored = list()
        # Queue for search
        self.search_steps = list()
        # paths for each position
        self.paths = dict()
    
    def move(self, row, col, path):
        
        temp_steps = list()
        # Uniform search: f(n) = g(n)
        
        # Check Up
        if row > 0:
            if self.grid[row - 1][col] != '%' \
               and (row - 1, col) not in self.visited:
                # calculate cost of by distance from initial pos 
                tmp_cost = abs(self.food_pos_r - (row - 1)) + abs(self.food_pos_c - col)
                # add next position with cost to temporary steps list
                temp_steps.append((row -1, col, tmp_cost))
                # add position to visited positions
                self.visited.append((row - 1, col))
                # assign path to that position
                self.paths[(row - 1, col)] = path
            
        # Check Left
        if col > 0: 
            if self.grid[row][col - 1] != '%' \
               and (row, col - 1) not in self.visited:
                # calculate cost of by distance from initial pos 
                tmp_cost = abs(self.food_pos_r - (row - 1)) + abs(self.food_pos_c - (col - 1))
                # add next position with cost to temporary steps list
                temp_steps.append((row, col - 1, tmp_cost))
                self.visited.append((row, col - 1))
                self.paths[(row, col - 1)] = path
            
        # Check Right
        if col < self.width - 1:
            if self.grid[row][col + 1] != '%' \
               and (row, col + 1) not in self.visited:
                # calculate cost of by distance from initial pos 
                tmp_cost = abs(self.food_pos_r - (row - 1)) + abs(self.food_pos_c - col + 1)
                # add next position with cost to temporary steps list
                temp_steps.append((row, col + 1, tmp_cost))
                self.visited.append((row, col + 1))
                self.paths[(row, col + 1)] = path
            
        # Check Down
        if row < self.height - 1:
            if self.grid[row+1][col] != '%' \
               and (row + 1, col) not in self.visited:
                # calculate cost of by distance from initial pos 
                tmp_cost = abs(self.food_pos_r - (row + 1)) + abs(self.food_pos_c - col)
                # add next position with cost to temporary steps list
                temp_steps.append((row + 1, col, tmp_cost))
                self.visited.append((row + 1, col))
                self.paths[(row + 1, col)] = path
                
        sorted_steps = sorted(temp_steps, key=lambda step: step[2])
        for step in sorted_steps:
            self.search_steps.append(step[:2])

            
            
    def uniform_cost_search(self):
        
        self.search_steps.append((self.pac_pos_r, self.pac_pos_c))
        self.visited.append((self.pac_pos_r, self.pac_pos_c))
        
        while len(self.search_steps) > 0:
            
            # get top position
            current_row, current_col = self.search_steps[0]
            self.search_steps = self.search_steps[1:]
            
            # add it to explored positions
            self.explored.append((current_row, current_col))
            
            # get path of that position 
            path = self.paths.get((current_row, current_col), list()).copy()
            
            # add current position to path for new assignments
            path.append((current_row, current_col))
            # If food is found
            if current_row == self.food_pos_r and current_col == self.food_pos_c:
                # get path of food
                path = self.paths[(current_row, current_col)]
                path.append((current_row, current_col))
                    
                # print path to food 
                print(len(path) - 1)
                for row, col in path:
                    print(f'{row} {col}')
                    
                return
            # If could not find food check new positions
            self.move(current_row, current_col, path)    
        
        
if __name__ == "__main__":
    pac_pos_r, pac_pos_c = [int(val) for val in input().split(' ')]
    food_pos_r, food_pos_c = [int(val) for val in input().split(' ')]
    rows, columns = [int(val) for val in input().split(' ')]
    grid = list()
    for i in range(rows):
        grid.append([val for val in input()])
    pacman = PacMan(pac_pos_r=pac_pos_r,
                    pac_pos_c=pac_pos_c,
                    food_pos_r=food_pos_r,
                    food_pos_c=food_pos_c,
                    width=columns,
                    height=rows,
                    grid=grid)
    pacman.uniform_cost_search()