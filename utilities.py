from random import randint
from math import sqrt
import random
import string

def generate_int_list():
    """Returns a list with n randomly generated integers.
       You may use set_constants() function to set parameter values
       Range: From min_val to max_val
    """
    array_length = randint(9, 11)
    array = [None] * array_length
    min_val = randint(1, 100)
    max_val = min_val * 50
    for i in range(array_length):
        num = randint(min_val, max_val)
        array[i] = num
    return array

def generate_str_list():
    """Returns a list with of strings
       Parameter values must be set by the calling function
       string_length: length of each string
       array_length: No. of strings in the list
       array: Placeholder for name of the list
    """
    array_length = randint(9, 11)
    string_length = randint(5, 10)
    array = [None] * array_length
    for i in range(array_length):
        p = ''.join(random.choices(string.ascii_uppercase + string.digits, k = string_length))
        array[i] = p
    return array 

def generate_2D_points():
    """Generates list of points in 2D space. Each point is represented by a list with two elements.
       array_length: Number of points in the list. A random number
       array: the list of points
    """
    #array_length = randint(100, 200)
    array_length = 6
    array = [[randint(-1000, 1000), randint(-1000, 1000)] for i in range(array_length)]
    return array

def find_distance_2D(points):
    """Computes distances between 2D points. Returns a square symmetric matrix of dimension N, 
       where N is the number of points in the array.
       Diagonal elements are zero as they represent the distance from a point to itself.
       points: list containing the points. Each point is also a list with two elements
       distances: A 2D array in which the distances are stored. Initialis this array to
       zero before calling the function.
    """
    N = len(points) # Number of points
    distances = [[0 for row in range(N)] for col in range(N)]
    for i in range(N):
        for j in range(N):
            if i < j:
                distances[i][j] = sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
                distances[i][j] = round(distances[i][j], 2)
            if i > j:
                distances[i][j] = distances[j][i]
    return distances 

def matrix_to_1D_array(matrix):
    """Writes the upper diagonal elements of a square matrix to a linear array.
       Diagonal elements are not considered, as they are zero.
       Mapping from 2D array to 1D array is based on the formula given here:
       https://math.stackexchange.com/questions/2134011/conversion-of-upper-triangle-linear-index-from-index-on-symmetrical-array

       Keyword arguments:
       N -- Dimension of the square matrix
       matrix -- A square, symmetric matrix. All diagonal elements are zero
    """
    N = len(matrix) #Dimension of the matrix
    array_length_1D = int(N * (N-1)/2)
    array_distances_1D = [0 for i in range(array_length_1D)] #1D array of distances
    for i in range(N):
        for j in range(N):
            if i < j:
                array_index_1D = int(array_length_1D - ((N - i)*(N - i - 1)/2) + j) - (i + 1)
                array_distances_1D[array_index_1D] = matrix[i][j]
    return array_distances_1D

def display_matrix(matrix):
    """Displys 2D lists in matrix form"""
    for rows in range(len(matrix)):
        print(matrix[rows])

def verify_sort(array):
    """Verifies sort and returns boolean.
       Returns True if the list elements are sorted in increasing order
       Returns False for other cases.

       Keyword arguments:
       array -- Sorted list
    """
    array_length = len(array)
    for i in range(0, array_length-1):
        if array[i] > array[i+1]:
            return "List is not sorted." 
            #result = False
        else:
            return "Sorting is verified."
            #result = True

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
    array_length, array = generate_2D_points()
    distances = [[0 for i in range(array_length)] for j in range(array_length)]