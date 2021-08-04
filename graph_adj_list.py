
class GraphAdjNode:
    def __init__(self,data) -> None:
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = [None] * vertices
    
    def addEdge(self, src, dest):

        node = GraphAdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = GraphAdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def deleteEdge(self, src, dest):
        node = self.graph[src]
        if(node.vertex == dest):
            self.graph[src] = node.next
        else:
            temp = node.next
            prev = node
            while temp:
                if(temp.vertex == dest):
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next

    def printGraph(self):

        for i in range(self.V):
            print('{}'.format(i),end = " ")
            temp = self.graph[i]
            while temp:
                print('-> {}'.format(temp.vertex),end="")
                temp = temp.next
            print("\n")

if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0,1)
    graph.addEdge(0,4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.deleteEdge(1,3)
    graph.printGraph()