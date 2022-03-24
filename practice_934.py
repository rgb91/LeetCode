class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def distance(i, j, m, n):
            return abs(i-m) + abs(j-n)
                
        
        def getFirstOne(grid: List[List[int]]) -> Tuple[int, int]:
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == 1:
                        return (i, j)
        
        def traverseFirstIsland(grid: List[List[int]], i: int, j: int, visited: List[List[bool]], island_map):
            if i < 0 or j < 0 or i >= N or j >= N:
                return False
            
            print(i, j, grid[i][j], visited[i][j])
            
            if visited[i][j]:
                return True
            
            if grid[i][j]:
                visited[i][j] = True
                island_map[1].append((i, j))
                
                r1 = traverseFirstIsland(grid, i-1, j, visited, island_map)
                r2 = traverseFirstIsland(grid, i, j-1, visited, island_map)
                r3 = traverseFirstIsland(grid, i+1, j, visited, island_map)
                r4 = traverseFirstIsland(grid, i, j+1, visited, island_map)
                
                return r1 or r2 or r3 or r4
            
            return False
        
        N = len(grid)
        visited = [[False for i in range(N)] for j in range(N)]
        island_map = {1: [], 2: []}
        
        ix, jx = getFirstOne(grid)
        traverseFirstIsland(grid, ix, jx, visited, island_map)
        print(visited)

        for i in range(N):
            for j in range(N):
                if not visited[i][j] and grid[i][j]:
                    island_map[2].append((i, j))
                    
        print(island_map)
        
        min_dist = 999
        found = False
        for i, j in island_map[1]:
            for m, n in island_map[2]:
                dist = distance(i, j, m, n)
                # print('(',i,j,')', '(',m,n,')', dist)
                if dist < min_dist:
                    min_dist = dist
                if min_dist == 2: 
                    found = True
                    break
            if found:
                break
        
        return min_dist-1