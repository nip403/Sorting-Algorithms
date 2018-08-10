# Sorting-Algorithms
A visual representation of sorting algorithms in Python 3.x using the Pygame library.\
To run, open main.py.

Some of the fastest algorithms are (including graphically):
- Quicksort
- Mergesort
- Heapsort
- Radix sort
- Shellsort
- Binary Insertion sort
- Strand sort

Some of the slowest algorithms are:
- Bubble sort
- Insertion sort
- Selection sort
- Bogo sort
- Permutation sort

# Requirements
I am using the [Python 3.7](https://www.python.org/downloads/release/python-370/) IDLE.\
Download project and run main.py to use.\
Python 3.6 and Pygame 1.7.x or above is required.\
You can download pygame either [here](https://www.pygame.org/download.shtml) or [here](https://bitbucket.org/pygame/pygame/downloads/).

If you are running any version before 3.6, you will need to rewrite all f-strings using either of the following:
- % operator
- format() method

# Efficiencies

|Name|![](https://placehold.it/15/00ff00/000000?text=+) Best Case|![](https://placehold.it/15/ffff00/000000?text=+) Average Case|![](https://placehold.it/15/ff0000/000000?text=+) Worst Case|
|-|-|-|-|
|Quicksort|O(n log n)|O(n log n)|O(n^2)|
|Bubble sort|O(n)|O(n^2)|O(n^2)|
|Selection sort|O(n^2)|O(n^2)|O(n^2)|
|Cocktail Shaker sort|O(n)|O(n^2)|O(n^2)|
|Bogo sort|O(n)|O((n+1)!)|O(Infinity)|
|Odd-Even sort|O(n)|O(n^2)|O(n^2)|
|Shell sort (original gap sequence)|O(n log n)|O(n^2)|O(n^2)|
|Comb sort|O(n log n)|O(n^2 / 2^p)|O(n^2)|
|Insertion sort|O(n)|O(n^2)|O(n^2)|
|Merge sort (TopDown, out of place)|O(n log n)|O(n log n)|O(n log n)|
|Radix sort (LSD, base 256)|O(wn)|O(wn)|O(wn)|
|Counting sort|O(n+k)|O(n+k)|O(n+k)|
|Cycle sort|O(n^2)|O(n^2)|O(n^2)|
|Heap sort|O(n log n)|O(n log n)|O(n log n)|
|Circle sort|O(n log n)|O(n log n log n)|O(n log n log n)|
|Gnome sort|O(n)|O(n^2)|O(n^2)|
|Binary Insertion sort|O(n)|O(n log n)|O(n log n)|
|Pancake sort|O(n log n)|O(n log n)|O(n log n)|
|Permutation sort|O(n)|O(n * n!)|O(n * n!)|
|Strand sort|O(n)|O(n^2)|O(n^2)|
|Bucket sort|O(n+k)|O(n+k)|O(n^2)|
|MinMax sort|O(t=0,n//2 ∑ (n-2t))|O(t=0,n//2 ∑ (n-2t))|O(t=0,n//2 ∑ (n-2t))|
|Merge sort (BottomUp, out of place)|O(n log n)|O(n log n)|O(n log n)|

ADDITIONAL INFO:
- Comb Sort: p = amount of increments
- Radix Sort: w = word size
- Counting and Bucket Sort: k = range of inputs
- MinMax sort: sum of n-2t from t=0 to t=n//2

# Problems
- Validate Circle sort's average case time complexity
- Validate Shell sort's average case time complexity

# To-do List
- Bitonic Sort
- Radix Sort (MSD)
- Quicksort (2 pivots)
