
import doctest

def add(*args):
    """
    >>> matrix1 = [[1, -2], [-3, 4]]
    >>> matrix2 = [[2, -1], [0, -1]]
    >>> add(matrix1, matrix2)
    [[3, -3], [-3, 3]]
    >>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    >>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    >>> add(matrix1, matrix2)
    [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
    """
    
    rows = len(args[0])
    cols = len(args[0][0])

    for mat in args:
        if len(mat) != rows:
            raise ValueError("Invalid sizes")

        for row in mat:
            if len(row) != cols:
                raise ValueError("Invalid sizes")
            


    result = [[0]*len(args[0][0]) for x in range(len(args[0]))]

    for mat in args:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                result[i][j] += mat[i][j]


    return result


    


if __name__ == "__main__":
    doctest.testmod()