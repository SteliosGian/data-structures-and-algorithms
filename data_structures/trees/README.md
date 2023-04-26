# Trees

A Tree is a data structure in which data items are connected using references in a hierarchical manner.

## Binary Trees

Binary Tree is defined as a tree data structure where each node has at most 2 children. Since each element in a binary tree can have only 2 children, we typically name them the left and the right child.


**Time Complexity**
| Operation     | Big-O      |
| ------------- | -----------|
| lookup        | O(log N)   |
| insert        | O(log N)   |
| delete        | O(log N)   |

## Binary Search Tree (BST)

* The left subtree of a node contains only nodes with keys lesser than the node's key
* The right subtree of a node contains only nodes with keys greater than the node's key
* The left and right subtree each must also be a binary search tree

### Balanced VS Unbalanced BST

**Unbalanced BST**

**Time Complexity**
| Operation     | Big-O      |
| ------------- | -----------|
| lookup        | O(n)       |
| insert        | O(n)       |
| delete        | O(n)       |

### Pros & Cons

#### Pros

* Better than O(n)
* Ordered
* Flexible size

#### Cons

* No O(1) operations

## Binary Heaps

A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in the Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to Min Binary Heap.

Binary Heaps are good for doing comparative operations.

**Time Complecity**
| Operation     | Big-O      |
| ------------- | -----------|
| lookup        | O(n)       |
| insert        | O(log N)   |
| delete        | O(log N)   |

### Pros & Cons

#### Pros

* Better than O(n)
* Priority
* Flexible size
* Fast Insert

#### Cons

* Slow lookup

## Trie

A Trie is a multiway tree data structure used for storing strings over an alphabet. It is used to store a large amnounts of strings. The pattern matching can be done efficiently using Tries.
