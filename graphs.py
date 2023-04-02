'''
graphs
{
    'A':['B','E'],
    'B':['A','C'],
    'C':['B','D'],
    'D':['C','E'],
    'E':['A','D']
}

Adjency list 👆
Space complexity - O(|V|+|E|)

'''


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):  # Add a vertex
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):  # Add edge
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):  # Remove edge
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):  # Remove vertex
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
