from random import randint

def set_constants():
    array_length = randint(9000, 11000)
    array = [None] * array_length 
    min_val = randint(1, 100)
    max_val = array_length * 5
    return array_length, array, min_val, max_val

def generate_int_list(array_length, array, min_val, max_val):
    """Returns a list with n randomly generated integers.
       Range: From min_val to max_val"""
    for i in range(array_length):
        num = randint(min_val, max_val)
        array[i] = num
    return array

def generate_str_list(string_length, array_length, array):
    for i in range(array_length):
        p = ''.join(random.choices(string.ascii_uppercase + string.digits, k = string_length))
        array[i] = p
    return array
    



def verify_sort(array_length, x):
    """Returns boolean.
       Returns True if the list elements are sorted in increasing order
       Returns False for other cases.
    """
    for i in range(0, array_length-1):
        if x[i] > x[i+1]:
            result = False
        else:
            result = True
    return result 

if __name__ == "__main__":
    array_length, array, min_val, max_val = set_constants()
    x = generate_list(array_length, array, min_val, max_val)
