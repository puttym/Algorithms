from random import randint

n = randint(9000, 11000) # n lies between 9000 and 11000 (both included)
array = [None] * n # creates a list of length n 
min_value = randint(1, 100) # Lower bound for the values in the array
max_value = 5 * n # Upper bound for the values in the array

def generate_list(min_value, max_value): 
    """Returns a list with n randomly generated integers. 
       Range: min_value to max_value"""
    for i in range(n):
        num = randint(min_value, max_value)
        array[i] = num
    return array

def selection_sort(x):
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

def verify_sort(x):
    """Returns boolean.
       True if the list elements are sorted in increasing order.
       False in other cases."""
    for i in range(0, n-1):
        if x[i] > x[i+1]:
            return False
        else:
            result = True
    return result

def main():
    x = generate_list(min_value, max_value)
    sorted_x = selection_sort(x)
    print(verify_sort(sorted_x))

if __name__ == "__main__":
    main()
