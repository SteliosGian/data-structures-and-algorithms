# Hash Tables

```python
{
'key1': 'value1',
'key2': 'value2
}
```


| Operation     | Big-O      | Python Notation    |
| ------------- | -----------|------------------- |
| insert        | O(1)       |``` d['key'] = 'value ```|
| lookup        | O(1)       |``` d['key'] ```   |
| delete        | O(1)       |``` d.pop['key'] ```|

## Hash Collision

When we add in the same memory space. It slows down reading and writing with O(n/k), k = size of hash table, meaning O(n)

## Pros & Cons

### Pros

* Fast lookups (Good collision resolution needed)
* Fast inserts
* Flexible keys

### Cons

* Unordered (Python now uses ordered dicts)
* Slow key iteration
