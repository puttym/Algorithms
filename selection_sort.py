from random import randint
from utilities import generate_list, verify_sort, set_constants

def selection_sort(n, x):
    """Returns the list with elements sorted in increasing order.
       Algorithm: Selection sort"""
    for i in range(0, n-1):
        mim = x[i]
        for j in range(i+1, n):
            if x[j] < mim:
                mim = x[j]
                loc = j
        tmp = x[i]
        x[i] = mim
        x[loc] = tmp
    return x

def main():
    n, array, min_val, max_val = set_constants()
    x = generate_list(n, array, min_val, max_val)
    sorted_x = selection_sort(n, x)
    print(verify_sort(n, sorted_x))

if __name__ == "__main__":
    main()
