"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self ,grid):
        # Check if given grid is null
        if grid is None:
            return 0

        row = len(grid)
        column = len(grid[0])

        # Define counter to count no of islands
        islandcount = 0

        for i in range(0, row):
            for j in range(0, column):

                if grid[i][j] == '1':
                    islandcount += 1

                    self.changeLandtoWater(grid, i, j)
        return islandcount

    def changeLandtoWater(self,grid, i, j):

        if i  < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        
        self.changeLandtoWater(grid, i-1, j) # up
        self.changeLandtoWater(grid, i+1, j) # down
        self.changeLandtoWater(grid, i, j-1) # left
        self.changeLandtoWater(grid, i, j+1) # right
