from utilities import generate_int_list, verify_sort, set_constants

def selection_sort(array_length, x):
    """Returns the list with elements sorted in increasing order.
       Algorithm: Selection sort"""
    for i in range(0, array_length-1):
        mim = x[i]
        for j in range(i+1, array_length):
            if x[j] < mim:
                mim = x[j]
                loc = j
        tmp = x[i]
        x[i] = mim
        x[loc] = tmp
    return x

def main():
    array_length, array, min_val, max_val = set_constants()
    x = generate_int_list(array_length, array, min_val, max_val)
    sorted_x = selection_sort(array_length, x)
    print(verify_sort(array_length, sorted_x))

if __name__ == "__main__":
    main()
