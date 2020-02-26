from random import randint
from utilities import generate_int_list, verify_sort, set_constants

def bubble_sort(array_length, a):
    """Sorts an array of numbers in increasing order.
       a - array"""
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                t1 = a[j]
                t2 = a[j+1]
                a[j] = t2
                a[j+1] = t1
    return a

def main():
    array_length, array, min_val, max_val = set_constants()
    x = generate_int_list(array_length, array, min_val, max_val)
    sorted_x = bubble_sort(array_length, x)
    print(verify_sort(array_length, sorted_x))

if __name__ == "__main__":
    main()