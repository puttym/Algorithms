from random import randint
from utilities import generate_list, verify_sort, set_constants

def bubble_sort(n, a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                t1 = a[j]
                t2 = a[j+1]
                a[j] = t2
                a[j+1] = t1
    return a

def main():
    n, array, min_val, max_val = set_constants()
    x = generate_list(n, array, min_val, max_val)
    sorted_x = bubble_sort(n, x)
    print(verify_sort(n, sorted_x))

if __name__ == "__main__":
    main()
