import sys

class Graph:
    def __init__(self,vertices) -> None:
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def printDistance(self,src,dist):
        for node in range(self.V):
            print('{}->{} = {}'.format(src,node,dist[node]))


    def minDistance(self, dist, visited):
        min = sys.maxsize

        for v in range(self.V):
            if(dist[v]<min and visited[v] == False):
                min = dist[v]
                min_index = v
            
        return min_index

    def dijkstra(self,src):

        dist = [sys.maxsize] * self.V
        visited = [False] * self.V
        dist[src] = 0

        for i in range(self.V):
            u = self.minDistance(dist,visited)

            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v]>0 and visited[v] == False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        
        self.printDistance(src, dist)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
    g.dijkstra(0)