# Linked Lists

```
basket = ['apples', 'grapes', 'pears']
linked list: apples --> grapes --> pears

apples
8947 --> grapes
         8742 --> pears
                  372 --> null
```

A **Linked List** contains a set of nodes. Each node has the value of the data and a pointer to the next node. First node is the head and last node is the tail. Linked lists are null terminated.

## Time Complexity

| Operation     | Big-O      |
| ------------- | -----------|
| prepend       | O(1)       |
| append        | O(1)       |
| lookup        | O(n)       |
| insert        | O(n)       |
| delete        | O(n)       |

## Doubly Linked List

A Doubly Linked List's node also points to the previous node but it consumes more memory.


## Single vs Double

* Single has simple implementation
* Single has less memory
* Single cannot be traversed in reverse
* Single for less memory and fast insertion and deletion
* Double is more complex and requires more memory

## Pros & Cons

### Prod

* Fast insertion
* Fast deletion
* Ordered
* Flexible size

### Cons

* Slow lookup
* More memory
