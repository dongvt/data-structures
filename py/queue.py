from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        #Special case: the first cell is not 0
        if grid[0][0] != 0:
            return -1
        
        #Helper function to get all the valid neighbors
        def getNeighbors(cell):
            #Directions contain the coordinates for all the possible neighbors
            directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            
            for direction in directions:
                #compute neighbors
                newRow = cell[0] + direction[0]
                newCol = cell[1] + direction[1]
                
                #Check index out of bounds
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue
                
                #Ignore non 0 cells (we just can go through 0 cells)
                if grid[newRow][newCol] != 0:
                    continue
                
                #This is to iterate this function
                yield (newRow,newCol)

        q = deque()
        
        q.append((0,0))
        grid[0][0] = 1
        
        while(len(q) > 0):
            cell= q.popleft() #pop the current cell
            distance = grid[cell[0]][cell[1]] #store the value in the cell
            
            #If we reached the end stop the function and return the distance
            if cell == (len(grid) - 1,len(grid[0]) - 1):
                return distance
            
            for neighbor in getNeighbors(cell):
                #Get the neighbor and change its value by adding one to the current distance
                #Remember we already ignored all invalid cells
                grid[neighbor[0]][neighbor[1]] = distance + 1
                #Enqueue the new cell
                q.append(neighbor)
        
        return -1