# Sorting-Algorithms
A visual representation of sorting algorithms in Python 3.x using the Pygame library.\

# Installation

You can download the zipped version above, or (if you're using Windows) run the following in your command line:

```
git clone https://github.com/nip403/Sorting-Algorithms.git Desktop && cd Sorting-Algorithms-master
```

# Execution

After the installation, you should be located in the correct directory. If not, run the following:

```
cd Desktop\Sorting-Algorithms-master
```

Then, to run:

```
py main.py
```

# Requirements
I am using the [Python 3.7](https://www.python.org/downloads/release/python-370/) IDLE.\
Download project and run main.py to use.\
Python 3.6 and Pygame 1.7.x or above is required.\
You can download pygame either [here](https://www.pygame.org/download.shtml) or [here](https://bitbucket.org/pygame/pygame/downloads/).

If you are running any version before 3.6, you will need to rewrite all f-strings using either of the following:
- % operator
- format() method

# Algorithms

|Name|![](https://placehold.it/15/00ff00/000000?text=+) Best Case|![](https://placehold.it/15/ffff00/000000?text=+) Average Case|![](https://placehold.it/15/ff0000/000000?text=+) Worst Case|Space Complexity|Usability|
|-|-|-|-|-|-|
|Quicksort|O(n log n)|O(n log n)|O(n^2)|O(n)|★★★★★|
|Bubble sort|O(n)|O(n^2)|O(n^2)|O(1)|★★☆☆☆|
|Selection sort|O(n^2)|O(n^2)|O(n^2)|O(1)|★★☆☆☆|
|Cocktail Shaker sort|O(n)|O(n^2)|O(n^2)|O(1)|★★★☆☆|
|Bogo sort|O(n)|O((n+1)!)|O(Infinity)|O(n)|☆☆☆☆☆|
|Odd-Even sort|O(n)|O(n^2)|O(n^2)|O(1)|★★★☆☆|
|Shell sort (original gap sequence)|O(n log n)|O(n^2)|O(n^2)|O(1)|★★★★☆|
|Comb sort|O(n log n)|O(n^2 / 2^p)|O(n^2)|O(1)|★★★☆☆|
|Insertion sort|O(n)|O(n^2)|O(n^2)|O(1)|★★☆☆☆|
|Merge sort (TopDown, out of place)|O(n log n)|O(n log n)|O(n log n)|O(n)|★★★★★|
|Radix sort (LSD, base 256)|O(wn)|O(wn)|O(wn)|O(n+W)|★★★★★|
|Counting sort|O(n+k)|O(n+k)|O(n+k)|O(n+k)|★★★☆☆|
|Cycle sort|O(n^2)|O(n^2)|O(n^2)|O(1)|★★☆☆☆|
|Heap sort|O(n log n)|O(n log n)|O(n log n)|O(1)|★★★★★|
|Circle sort|O(n log n)|O(n log n log n)|O(n log n log n)|O(n)|★★★☆☆|
|Gnome sort|O(n)|O(n^2)|O(n^2)|O(1)|★★☆☆☆|
|Binary Insertion sort|O(n)|O(n log n)|O(n log n)|O(1)|★★★☆☆|
|Pancake sort|O(n log n)|O(n log n)|O(n log n)|O(1)|★★★☆☆|
|Permutation sort|O(n)|O(n!)|O(n!)|O(n)|★☆☆☆☆|
|Strand sort|O(n)|O(n√n)|O(n^2)|O(n)|★★★☆☆|
|Bucket sort|O(n+k)|O(n+k)|O(n^2)|O(n * k)|★★★★☆|
|MinMax sort|t=0,n//2 ∑ (n-2t)|t=0,n//2 ∑ (n-2t)|t=0,n//2 ∑ (n-2t)|O(2)|★★★☆☆|
|Merge sort (BottomUp, out of place)|O(n log n)|O(n log n)|O(n log n)|O(n)|★★★★★|

ADDITIONAL INFO:
- Best case, average case and worst case all describe the algorithm's time complexity
- All space complexities are auxiliary. Total space complexity is always O(n)
- Comb Sort: p = amount of increments
- Radix Sort: W = maximum number of digits, w = word size or significant digits
- Counting and Bucket Sort: k = range of inputs
- MinMax sort: sum of n-2t from t=0 to t=n//2

# Problems
- Validate Circle sort's average case time complexity and space complexity
- Validate Shell sort's average case time complexity
- Convert MinMax Sort's time complexities from summations into big O notation
- Validate Strand Sort's space complexity

# To-do List
- Radix Sort (MSD)
- Quicksort (2 pivots)
