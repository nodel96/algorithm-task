def _merge(a, lo, mid, hi, aux):
    """
    Merge function for mergesort.
    Merges two sorted subarrays a[lo:mid] and a[mid:hi] into a single sorted subarray a[lo:hi].
    """
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:
            aux[k] = a[j]
            j += 1
        elif j == hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1
    a[lo:hi] = aux[0:n]

def _sort(a, lo, hi, aux):
    """
    Recursive sorting function for mergesort.
    Sorts the subarray a[lo:hi] using an auxiliary array aux.
    """
    n = hi - lo
    if n <= 1:  # Base case: nothing left to do
        return
    mid = (lo + hi) // 2
    _sort(a, lo, mid, aux)
    _sort(a, mid, hi, aux)
    _merge(a, lo, mid, hi, aux)

def mergesort(a):
    """
    Mergesort implementation.
    Sorts the input array a using the mergesort algorithm.
    """
    n = len(a)
    aux = [None] * n  # Create an empty auxiliary array
    _sort(a, 0, n, aux)  # Sort the array a in the range [0:n]
    
# Example usage:
import random

# Generate a random shuffled array
a = list(range(10))
random.shuffle(a)
print("Original array:", a)

# Sort the array using mergesort
mergesort(a)
print("Sorted array:", a)
