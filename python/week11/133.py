# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.nodes = {}

    def cloneGraph(self, node):
        new_node = None
        if node:
            if node.label in self.nodes:
                new_node = self.nodes[node.label]
            else:
                new_node = UndirectedGraphNode(node.label)
                self.nodes[new_node.label] = new_node
                for neighbor in node.neighbors:
                    new_node.neighbors.append(self.cloneGraph(neighbor))
        return new_node
