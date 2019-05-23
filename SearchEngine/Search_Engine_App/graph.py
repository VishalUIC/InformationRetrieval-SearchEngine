class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if not node in self.graph.keys() and len(node) > 1:
            self.graph[node] = {}

    def add_edge_weight(self, node_1, node_2):
        if (len(node_1) <= 1) or (len(node_2) <= 1):
            return
        if node_2 in self.graph:
            if node_1 not in self.graph[node_2].keys():
                self.graph[node_2][node_1] = 1
            else:
                self.graph[node_2][node_1] += 1
            if node_2 not in self.graph[node_1].keys():
                self.graph[node_1][node_2] = 1
            else:
                self.graph[node_1][node_2] += 1

    def get_adjacent(self, node):
        if node in self.graph.keys():
            return list(self.graph[node].keys())
        else:
            return []

    def get_edge_weight(self, node_1, node_2):
        if (node_1 in self.graph.keys()) and (node_2 in self.graph.keys()):
            return self.graph[node_1][node_2]
        else:
            return 0
