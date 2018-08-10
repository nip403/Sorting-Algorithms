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

# Requirements
I am using the [Python 3.7](https://www.python.org/downloads/release/python-370/) IDLE.\
Download project and run main.py to use.\
Python 3.6 and Pygame 1.7.x or above is required.\
You can download pygame either [here](https://www.pygame.org/download.shtml) or [here](https://bitbucket.org/pygame/pygame/downloads/).

If you are running any version before 3.6, you will need to rewrite all f-strings using either of the following:
- % operator
- format() method

# Efficiencies
- Quicksort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Bubble Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Selection Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n^2)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Cocktail Shaker Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Bogo Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O((n+1)!)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(Infinity)`
- Odd-Even Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Shell Sort (Using original gap sequence)
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^1.5)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Comb Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2 / 2^p), p = amount of increments`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Insertion Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Merge Sort (TopDown, out of place)
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n log n)`
- Radix Sort (LSD, base 256)
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(nk)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(nk)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(nk)`
- Counting Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n+k)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n+k)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n+k)`
- Cycle Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n^2)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Heap Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n log n)`
- Circle Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n log n log n)`
- Gnome Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Binary Insertion Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n log n)`
- Pancake Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n log n)`
- Permutation Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n * n!)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n * n!)`
- Strand Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n^2)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Bucket Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n+k)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n+k)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n^2)`
- Minmax Sort
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(t=0,n//2 ∑ (n-2t)), (sum of n-2t from t=0 to t=n//2)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(t=0,n//2 ∑ (n-2t))`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(t=0,n//2 ∑ (ln-2t))`
- Merge Sort (BottomUp, out of place)
    - ![](https://placehold.it/15/00ff00/000000?text=+) `Best Case: O(n log n)`
    - ![](https://placehold.it/15/ffff00/000000?text=+) `Average Case: O(n log n)`
    - ![](https://placehold.it/15/ff0000/000000?text=+) `Worst Case: O(n log n)`

# Problems
- Validate Circle sort's average case time complexity
- Validate Shell sort's average case time complexity

# To-do List
- Bitonic Sort
- Radix Sort (MSD)
- Quicksort (2 pivots)
