from utilities import generate_str_list, set_constants, generate_int_list, verify_search
from selection_sort import selection_sort

def sequential_search(array, key):
    """Searches for an element in a list
       Element can either be a number or a string
       array - the list of elements. Need not be sorted
       key - the element to be searched"""
    index = 0
    while index < len(array):
        if array[index] == key:
            return index
        index += 1
    return -1

def sequential_sort_and_search(array, key):
    """Sort first and then search.
       Requires a sorted list
       array: list of elements sorted in increasing order
       key: element to be searched"""
    index = 0
    while key >= array[index]:
        if key == array[index]:
            return index
        index += 1
    return -1

def main():
    # Search for a number
    array_length, array, min_val, max_val = set_constants()
    x = generate_int_list(array_length, array, min_val, max_val)
    x = selection_sort(array_length, x)
    #index = sequential_sort_and_search(array = x, key = 147)
    index = sequential_search(array = x, key = 147)
    print(verify_search(array = x, index = index, key = 147))

#   Search for a string
#    from random import randint
#    array_length = randint(9000, 11000)
#    string_length = 5
#    array = [None] * array_length
#    x = generate_str_list(string_length, array_length, array)
#    print(sequential_search(array = x, key = 'ADFG45'))


if __name__ == "__main__":
    main()