from random import randint

def set_constants():
    n = randint(9000, 11000)
    array = [None] * n
    min_val = randint(1, 100)
    max_val = n * 5
    return n, array, min_val, max_val

def generate_list(n, array, min_val, max_val):
    """Returns a list with n randomly generated integers.
       Range: From min_val to max_val"""
    for i in range(n):
        num = randint(min_val, max_val)
        array[i] = num
    return array

def verify_sort(n, x):
    """Returns boolean.
       Returns True if the list elements are sorted in increasing order
       Returns False for other cases.
    """
    for i in range(0, n-1):
        if x[i] > x[i+1]:
            result = False
        else:
            result = True
    return result 

if __name__ == "__main__":
    n, array, min_val, max_val = set_constants()
    x = generate_list(n, array, min_val, max_val)
