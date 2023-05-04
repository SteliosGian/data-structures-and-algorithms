# Searching

## Linear Search

Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, otherwise the search continues till the end of the data set.

**Time Complexity** --> O(n)  
**Space Complexity** --> O(1)

## Binary Search

Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log n).

**Time Complexity** --> O(log n)  
**Space Complexity** --> O(1)

## Breadth-First Search - (BFS)

The Breadth-First Search (BFS) algorithm is used to search a tree or graph data structure for a node that meets a set of criteria. It starts at the tree's root or graph and searches/visits all nodes at the current depth level before moving on to the nodes at the next depth level. Breadth-first search can be used to solve many problems in graph theory.

## Depth-First Search - (DFS)

The Depth-First Search (DFS) follows one branch of the tree down as many levels as possible until the target node is found or the end is reached. If the end is reached, it continues to the nearest ancestor with an unexplored child.

## BFS vs DFS

### BFS

**Pros**

* Shortest path
* Closer nodes

**Cons**

* More memory

### DFS

**Pros**

* Less memory
* Does path exist?

**Cons**

* Can get slow


## BFS or DFS?

1. If you know a solution is not far from the root of the tree --> BFS

2. If the tree is very deep and solutions are rare --> BFS (DFS will take long)

3. If the tree is very wide --> DFS (BFS will need too much memory)

4. If solutions are frequent but located deep in the tree --> DFS

5. Determining whether a path exists between two nodes --> DFS

6. Finding the shortest path --> BFS


## How to solve the shortest path problem in weighted Graphs?

* Dijkstra Algorithm - More efficient and faster

* Bellman-Ford Algorithm - It can accommondate negative weights but takes a long time to run O(n^2)
