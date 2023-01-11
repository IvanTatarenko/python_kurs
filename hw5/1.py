def colums(mat_n, mat_m):
    mat = []
    while(mat_n > 0):
        if(mat_n == mat_m): mat.append(1)
        else: mat.append(0)
        mat_n -= 1
    return(mat)

def eye_matrix(size):
    mat = []
    mat_m = size
    while (mat_m > 0):
        mat.append(colums(size, mat_m))
        mat_m -= 1
    return(mat)

assert eye_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert eye_matrix(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

