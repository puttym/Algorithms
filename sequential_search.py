from utilities import generate_str_list, set_constants

def sequential_search(key, array):
    index = 0
    while index < len(array):
        if array[index] == key:
            return index
        index += 1
    return -1

def main():
    array_length, array, min_val, max_val = set_constants()
    string_length = 5
    x = generate_str_list(string_length, array_length, array)
    print(sequential_search(key = '10089', array = x))

if __name__ == "__main__":
    main()