# Graphs — Graph Theory Algorithms

This folder contains several classic graph theory algorithms.  
Graphs are fundamental data structures in computer science, representing relationships between objects (nodes/vertices) through connections (edges/arcs).

---

## Available Algorithms

- **A\* (A Star)**  
  Path finding algorithm with heuristics, widely used in artificial intelligence and video games.

- **BFS (Breadth-First Search)**  
  Level by level graph traversal, explores all nodes at the current depth before moving to nodes at the next depth level.

- **DFS (Depth-First Search)**  
  Explores a path to its end before backtracking, useful for maze solving and topological sorting.

- **Bellman-Ford**  
  Finds shortest paths from a source vertex, handles negative weights.

  [Python](./bellman_ford/python/bellman_ford.py), [Typescript](./bellman_ford/typescript/bellman_ford.ts)

- **Dijkstra**  
  Efficient algorithm for finding shortest paths in graphs with positive weights.

- **Floyd-Warshall**  
  Computes shortest paths between all pairs of vertices.

- **Kosaraju**  
  Finds strongly connected components in a directed graph.

- **Kruskal**  
  Constructs a minimum spanning tree using a greedy approach.

- **Prim**  
  Alternative to Kruskal's algorithm for building minimum spanning trees.

- **Tarjan**  
  Finds strongly connected components, more efficient than Kosaraju's algorithm.

- **Topological Sort**  
  Orders vertices in a directed acyclic graph according to their dependencies.

---

## Common Applications

- GPS Navigation and Routing
- Social Networks
- Network Optimization (Telecommunications, Transportation)
- Artificial Intelligence and Gaming
- Software Dependency Analysis
- Project Planning

---

Each algorithm is implemented in multiple programming languages, with its own unit tests to ensure reliability.

Feel free to contribute or ask questions!

---

## License

This project is under MIT license.
