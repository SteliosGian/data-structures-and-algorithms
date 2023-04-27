'''
Graphs representation and implementation
'''

# Edge List
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix
graph = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]


class Graph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        # Undirected Graph
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(node + "-->" + connections)


my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')

my_graph.show_connections()

# Answer
# 0 --> 1 2
# 1 --> 3 2 0
# 2 --> 4 1 0
# 3 --> 1 4
# 4 --> 3 2 5
# 5 --> 4 6
# 6 --> 5
