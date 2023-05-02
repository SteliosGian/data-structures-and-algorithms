# Sorting

A Sorting Algorithm is used to rearrange a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of elements in the respective data structure.

Time Complecity is measured in worst case.

## Bubble Sort

Bubble Sort repeatedly swaps the adjacent elements if they are in the wrong order.

**Time Complexity** --> O(n^2)  
**Space Complexity** --> O(1)

## Selection Sort

Selection Sort works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

**Time Complexity** --> O(n^2)  
**Space Complexity** --> O(1)

## Insertion Sort

In Insertion Sort, the array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
It is used when the list is almost/nearly sorted.

**Time Complexity** --> O(n^2)  
**Space Complexity** --> O(1)

## Merge Sort

Merge Sort works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

**Time Complexity** --> O(n log n)  
**Space Complexity** --> O(n)

## Quick Sort

Quick Sort is based on the divide and conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
When the pivot is the smaller or the larger item in the list, then quick sort ends up in time complexity of O(n^2).

**Time Complexity** --> O(n^2)  
**Space Complexity** --> O(log n)

## When to Use Each Algorithm

1. Insertion Sort: If input is small or items are almost sorted.
2. Merge Sort: When worried about worst case scenarios.
3. Quick Sort: Most popular but pivot must be chosen carefully.

## Heap Sort

Heap Sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the Selection Sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.  
Quick Sort is most of the times better than Heap Sort because Quick Sort does not do unnecessary element swaps which are time consuming.

**Time Complexity** --> O(n log n)  
**Space Complexity** --> O(1)

## Radix Sort - Non-Comparison Sort

Radix Sort is an integer sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (place value).

**Time Complexity** --> O(nk)  
**Space Complexity** --> O(n + k)

## Counting Sort - Non-Comparison Sort

Counting Sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (a kind of hashing). Then do some arithmetic operations to calculate the position of each object in the output sequence.

**Time Complexity** --> O(n + k)  
**Space Complexity** --> O(k)


# Sorting Problems (Choose an Algorithm)

1. Sort 10 schools around your house by distance --> Insertion sort

2. eBay sorts listings by the current Bid amount --> Radix or Counting sort

3. Sport scores on ESPN --> Quick sort

4. Massive database (can't fit all into memory) needs to sort through past year's user data --> Merge sort

5. Almost sorted review data needs to update and add 2 new reviews --> Insertion sort

6. Temperature records for the past 50 years in Canada --> Radix or Counting sort if temperature have no decimals, else Quick sort

7. Large user name database needs to be sorted. Data is very random. --> Merge sort or Quick sort

8. You want to teach sorting for the first time --> Bubble sort or Selection sort
