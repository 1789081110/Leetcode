class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        queue=[]
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append([i,j,0])
        ans=0
        while(queue):
            i,j,time=queue.pop(0)
            ans=time
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                dx,dy=i+x,j+y
                if (0<=dx<r  and 0<=dy<c and grid[dx][dy]==1):
                    grid[dx][dy]=2
                    queue.append([dx,dy,time+1])
        for a in grid:
            if 1 in a:
                return -1
        return ans                
'''
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
'''
