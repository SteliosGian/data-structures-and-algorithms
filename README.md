# Data Structures & Algorithms

This repo will include the most popular Data Structures and Algorithms along with some examples.

## Time Complexity - Big O

In simple terms, Big O notation shows us how scalable the code is, meaning how fast it can run with increasing number of input size.  
The Big O notations are the following:

### Chart
| Notation      | Explanation |
| ------------- | ----------- |
| O(1)          | Constant                                           |
| O(log N)      | Logarithmic - Sorted algorithms have usually log N |
| O(n)          | Linear - For loops or while looks through n items        |
| O(n log(n))   | Log linear - Usually sorting operations        |
| O(n^2)        | Quadratic - Nested loops, every element is compared to every other element        |
| O(2^n)        | Explonential - Recursive algorithms that solve a problem of size N       |
| O(n!)         | Factorial - A loop for every element        |


![Big-O](resources/big_o.jpeg "Big-O Chart")
source https://www.bigocheatsheet.com/

### Examples

**O(1)**
```python
def dummy_function(input: list) -> None:
    print("big-o")  # O(1)
```

**O(n)**
```python
def dummy_function(input: list) -> None:
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in input:
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)
    for j in input:
        p = j * 2  # O(n)
        q = j * 2  # O(n)
    
    c = "NoOne"  # O(1)
```
Big-O = O(4 + 5n) = O(n)

**O(n^2)**
```python
# Log all pairs of array
boxes = ['a','b','c','d','e']

def log_all_pairs_of_array(array: list) -> None:
    for i in array:
        for j in array:
            print(array[i], array[j])
```
Big-O = O(n * n) - O(n^2)


### Rules

1. We only care about the worst case
2. Remove constants
3. Different terms for inputs (e.g., O(a + b))
4. Drop non dominant terms (i.e., keep the highest)

## Good Code

* Readable
* Scalable
    * Speed
    * Memory

## Space Complexity

* Variables 
* Data Structures
* Function Call
* Allocations

### Examples

**O(1)**
```python
def dummy_function(input: list) -> None:
    for i in list:
        print("Time")
```

**O(n)**
```python
def dummy_function(input: list) -> list:
    array = []
    for i in input:
        array.insert(i, "Time")
    return array
```

## Data Structures

* Arrays
* 

## Algorithms

* 
* 
