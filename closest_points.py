from utilities import generate_2D_points, find_distance_2D, display_matrix, matrix_to_1D_array
from bubble_sort import bubble_sort
from math import sqrt

def find_closest_points(array, distances):
    """Returns closest among the given set of points and the distance between them.
       If the minimum distance is 1000000, then initialise min_dist to a much higher value
       array: list of 2D points
       distances: 2D matrix containing the distance between the points
    """
    min_dist = 1000000 #Deliberately initialising with a large value
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] != array[j]:
                if min_dist > distances[i][j]:
                    min_dist = distances[i][j]
                    point1 = array[i]
                    point2 = array[j]
    return min_dist, point1, point2

def verify_min_dist(array_length, array, distances):
    """Verifies the distance between the closest points. 
       Returns a message if test is successful. Returns False otherwise.
       The upper diagonal elements of the distance matrix, excluding the diagonal 
       elements, are written to a 1D-array. This array is then sorted and the first element 
       of the sorted array is the minimum distance.
    """
    min_dist, point1, point2 = find_closest_points(array, distances) 
    array_legth_1D, array_distances_1D = matrix_to_1D_array(array_length, distances)
    array_distances_1D = bubble_sort(array_legth_1D, array_distances_1D)
    if min_dist == array_distances_1D[0]:
        print('\nClosest points are',point1, 'and', point2, '.')
        print('\nDistance between them is', min_dist, 'units.')
        return "\nDistance between the closest points is verified."
    else:
        return False

def main():
    array_length, array = generate_2D_points()
    distances = [[0 for i in range(array_length)] for j in range(array_length)]
    distances = find_distance_2D(array, distances)
    print(verify_min_dist(array_length, array, distances))

if __name__ == '__main__':
    main() 