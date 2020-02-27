from random import randint
import random
import string

def set_constants():
    """Randomly generates numbers required for generating lists
       array_length: int; Lies between 9000 and 11000
       array: List initialised with 'None' as each element
       min_val: Lower bound for the values in array. A random int lying between 1 and 100
       max_val: Upper bound for the values in array. Equal to five times the number of 
       elements in the array
    """ 
    array_length = randint(9000, 11000)
    array = [None] * array_length 
    min_val = randint(1, 100)
    max_val = array_length * 5
    return array_length, array, min_val, max_val

def generate_int_list(array_length, array, min_val, max_val):
    """Returns a list with n randomly generated integers.
       You may use set_constants() function to set parameter values
       Range: From min_val to max_val
    """
    for i in range(array_length):
        num = randint(min_val, max_val)
        array[i] = num
    return array

def generate_str_list(string_length, array_length, array):
    """Returns a list with of strings
       Parameter values must be set by the calling function
       string_length: length of each string
       array_length: No. of strings in the list
       array: Placeholder for name of the list
    """
    for i in range(array_length):
        p = ''.join(random.choices(string.ascii_uppercase + string.digits, k = string_length))
        array[i] = p
    return array 

def verify_sort(array_length, x):
    """Verifies sort and returns boolean.
       Returns True if the list elements are sorted in increasing order
       Returns False for other cases.
    """
    for i in range(0, array_length-1):
        if x[i] > x[i+1]:
            result = False
        else:
            result = True
    return result 

def verify_search(array, index, key):
    """Veirfies the result of a search.
       array: A list
       key: Element to be searched in the array
       index: index of the element in the array, if found
       Returns True if array element matches the key
       Returns False if the array element doesn't match the key. This happens when the 'key'
       value is different in search and verification functions.
       Returns -1 if the element is not found in the list
    """
    if index != -1:
        if array[index] == key:
            return True
        else:
            return False
    return -1

if __name__ == "__main__":
    array_length, array, min_val, max_val = set_constants()
