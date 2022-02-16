class Grid():

    def __init__(self):

        self.grid = []
        for n in range(4):
            self.grid.append([None] * 4)

        self.grid[0][0] = 4
        self.grid[0][1] = 4
        self.grid[0][2] = 4
    
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

                        for c in range(len(self.grid[prev_cell + 1:-1])):
                            if self.grid[r][prev_cell + 1 + c] == None:
                                prev_cell = prev_cell + 1 + c
                                break

                    else:
                        prev_cell = cell
            
            empty_cell = None
            for cell in range(len(self.grid[r])):
                for c in range(len(self.grid[r])):
                    if self.grid[r][c] == None:
                        empty_cell = c
                        break
                
                if empty_cell != None:
                    for c in range(empty_cell, 4):
                        if self.grid[r][c] != None:
                            self.grid[r][empty_cell] = self.grid[r][c]
                            self.grid[r][c] = None
                            break
                else:
                    break
    
    def move_right(self):

        for r in range(4):
            prev_cell = None
            for cell in range(len(self.grid[r]) - 1, -1, -1):

                if self.grid[r][cell] != None:
                    
                    if prev_cell == None:
                        prev_cell = cell
                    
                    elif self.grid[r][cell] == self.grid[r][prev_cell]:
                        self.grid[r][prev_cell] *= 2
                        self.grid[r][cell] = None

                        for c in range(len(self.grid[:prev_cell]), -1, -1):
                            if self.grid[r][c] == None:
                                prev_cell = c
                                break

                    else:
                        prev_cell = cell
            
            empty_cell = None
            for cell in range(len(self.grid[r]) - 1, -1, -1):
                for c in range(len(self.grid[r]) - 1, -1, -1):
                    if self.grid[r][c] == None:
                        empty_cell = c
                        break
                
                if empty_cell != None:
                    for c in range(len(self.grid[r][:empty_cell + 1]) - 1, -1, -1):
                        if self.grid[r][c] != None:
                            self.grid[r][empty_cell] = self.grid[r][c]
                            self.grid[r][c] = None
                            break
                else:
                    break

    def move_up(self):

            for c in range(4):
                prev_cell = None
                for r in range(len(self.grid[c])):

                    if self.grid[r][c] != None:

                        if prev_cell == None:
                            prev_cell = r
                        
                        elif self.grid[r][c] == self.grid[prev_cell][c]:
                            self.grid[prev_cell][c] *= 2
                            self.grid[r][c] = None

                            for row in range(len(self.grid[prev_cell + 1:-1])):
                                if self.grid[prev_cell + 1 + row][c] == None:
                                    prev_cell = prev_cell + 1 + c
                                    break
                        
                        else:
                            prev_cell = r
                
                empty_cell = None
                for row in range(len(self.grid[c])):
                    for r in range(len(self.grid[c])):
                        if self.grid[r][c] == None:
                            empty_cell = r
                            break
                    
                    if empty_cell != None:
                        for r in range(empty_cell, 4):
                            if self.grid[r][c] != None:
                                self.grid[empty_cell][c] = self.grid[r][c]
                                self.grid[r][c] = None
                                break
                    else:
                        break

def main():
    thing = Grid()
    print("Initial grid:")
    for row in thing.grid:
        print(row)
    thing.move_left()
    print("After move left grid:")
    for row in thing.grid:
        print(row)

main()