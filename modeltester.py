class Grid():

    def __init__(self):

        # self.grid = []
        # for n in range(4):
        #     self.grid.append([None] * 4)

        self.grid = [[],
                     [],
                     [],
                     []]
    
    def move_left(self):

        for r in range(4):
            prev_cell = None
            for cell in range(len(self.grid[r])):

                if self.grid[r][cell] != None:
                    
                    if prev_cell == None:
                        prev_cell = cell
                    
                    elif self.grid[r][cell] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] *= 2
                        self.grid[r][cell] = None
                        self.score += self.grid[r][prev_cell]
                        move = True

                    else:
                        prev_cell = cell
            
            empty_cell = None
            for cell in range(len(self.grid[r])):
                for c in range(len(self.grid[r])):
                    if self.grid[r][c] == None:
                        empty_cell = c
                        break
                
                if empty_cell != None:
                    for c in range(len(self.grid[r][empty_cell:])):
                        if self.grid[r][empty_cell + c] != None:
                            self.grid[r][empty_cell] = self.grid[r][empty_cell + c]
                            self.grid[r][empty_cell + c] = None
                            move = True
                            break
                else:
                    break

def main():
    thing = Grid()
    print("Initial grid:")
    for row in thing.grid:
        print(row)
    thing.move_left()