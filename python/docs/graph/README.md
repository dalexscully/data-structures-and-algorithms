# Graphs

In order to represent a graph data structure, this file implements 3 classes: Graph, Vertex, Edge.

## Challenge

Represent a graph using an adjacency list. Support the following methods:

- add_node(value)
- add_edge(node1, node2)
- get_nodes()
- get_neighbors(node)
- size()

## Approach & Efficiency

The adjacency list is implemented as a hashmap, resulting in constant time O(1) lookups. The space complexity is O(n).

## API

- add_node(value): adds a node which has the provided value
- add_edge(node1, node2): adds an edge between 2 nodes in the graph
- get_nodes(): returns all nodes in the graph
- get_neighbors(node): returns all neighbor nodes of provided node
- size(): returns number of nodes in the graph
