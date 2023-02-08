from Vector4 import Vector4


def vector_to_matrix(v):
    m = [n for n in range(3)]
    m[0] = v.x
    m[1] = v.y
    m[2] = v.z
    return m


def vector4_to_matrix(v):
    m = vector_to_matrix(v)
    m.append(v.w)
    return m


def matrix_to_vector(m):
    l = []
    for i in range(len(m)):
        l.append([m[i][0]])
    return l


def matrix_to_vector4(m):
    r = Vector4(m[0][0], m[1][0], m[2][0], 0)
    if len(m) > 3:
        r.w = m[3][0]
    return r


def multiply_matrix_vector(a, vec):
    m = vector_to_matrix(vec)
    r = matrix_multiplication(a, m)
    return matrix_to_vector(r)


def multiply_matrix_vector4(a, vec):
    m = vector4_to_matrix(vec)
    r = matrix_multiplication(a, m)
    return matrix_to_vector4(r)


def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)

    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                tot = 0
                for k in range(columns_a):
                    tot += a[x][k] * b[k][y]
                result_matrix[x][y] = [tot]
        return result_matrix
    else:
        return None
