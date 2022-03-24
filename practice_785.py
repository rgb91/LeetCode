from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        white, red = -1, 1
        colors = [white for i in range(len(graph))]
        visited = 0
        for node in range(len(graph)):
            if colors[node] == white:
                q = [node]
                colors[node] = red
                visited += 1
                while q:
                    u = q.pop(0)
                    for v in graph[u]:
                        if colors[v] == colors[u]: return False
                        if colors[v] == white: 
                            colors[v] = colors[u] ^ 1  # toggle 0 (blue) and 1 (red)
                            visited += 1
                            q.append(v)
            if visited == len(graph): break
        
        return True

"""
Test cases:
[[3],[2,4],[1],[0,4],[1,3]]
[[1],[0,3],[3],[1,2]]
[[1,2,3],[0,2],[0,1,3],[0,2]]
[[1,3],[0,2],[1,3],[0,2]]
[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
[[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]

Expected outputs:
true
true
false
true
false
false
"""