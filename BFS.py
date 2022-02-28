from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def insertEdge(self,v1,v2):
        self.graph[v1].append(v2)
    def BFS(self,startNode):
        visited = set()
        st = []
        st.append(startNode)
        while(len(st)):
            cur = st.pop(0)
            print(cur, end="->")
            for vertex in self.graph[cur]:
                if(vertex not in visited):
                    st.append(vertex)
                    visited.add(vertex)

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)
g.BFS(2)