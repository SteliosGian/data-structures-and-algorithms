# Stacks & Queues

## Stacks

A data structure that stores items in LIFO - Last In First Out manner. In a stack, a new element is added at one end and an element is removed from that end only.

```python
from queue import LifoQueue

stack = LifoQueue(maxsize=3)
```

### Time Complexity

| Operation     | Big-O      |
| ------------- | -----------|
| lookup        | O(n)       |
| pop           | O(1)       |
| push          | O(1)       |
| peek          | O(1)       |

## Queues

A data structure that stores items in FIFO - First In First Out manner. In a queue, the least recently added item is removed first.

```python
from collections import deque

queue = deque()
```


### Time Complexity

| Operation     | Big-O      |
| ------------- | -----------|
| lookup        | O(n)       |
| enqueue       | O(1)       |
| dequeue       | O(1)       |
| peek          | O(1)       |


## Pros & Cons

### Pros

* Fast operations
* Fast peek
* Ordered

### Cons

* Slow lookup
