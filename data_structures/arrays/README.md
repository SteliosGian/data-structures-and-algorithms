# Arrays

```python
['a', 'b', 'c']
```


| Operation     | Big-O      | Python Notation    |
| ------------- | -----------|------------------- |
| lookup        | O(1)       |``` l[0] ```            |
| push          | O(1)       |``` l.append('a') ```   |
| insert        | O(n)       |``` l.insert(0, 'a') ```|
| delete        | O(n)       |``` l.remove('a') ```   |

## Static Arrays

* Fixed size


## Dynamic Arrays

* Dynamic size
* append can be O(n) depending on the reserved size of the list. More info [here](https://stackoverflow.com/a/33045038).


## Prod & Cons

### Pros

* Fast lookups
* Fast push/pop
* Ordered

### Cons

* Slow inserts
* Slow deletes
* Fixed size for static arrays
