def get_rotated_index(n, i, j):
    return j, n - i - 1

def matrix_print(matrix):
    result = ''
    for row in matrix:
        for val in row:
            result += '{:4}'.format(val)

        result += '\n'
    print(result)


def rotateImage(image):
    n = len(image) - 1

    for i in range(n):
        for j in range(i, n - i):
            (image[i][j], image[j][n - i], image[n - i][n - j], image[n - j][i]) = (
                image[n - j][i], image[i][j], image[j][n - i], image[n - i][n - j]
            )

    return image

print()

# matrix_print(rotateImage([[1, 2], [3, 4]]))
# matrix_print([[7, 4, 1], [8, 5, 2], [9, 6, 3]])
# matrix_print(rotateImage([[1,2,3], [4,5,6], [7,8,9]]))

matrix_print(rotateImage([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

# for j in range(n):
#     to_i = j
#     to_j = n - i - 1
#     print(i, j, '->', to_i, to_j)
#     # image[i][j], image[to_i][to_j] = image[to_i][to_j], image[i][j]
#     result[i][j] = image[to_i][to_j]

# (image[i][j], image[i][n - j], image[n - i][n - j], image[n - i][j]) = (
#     image[n - i][j], image[i][j], image[i][n - j], image[n - i][n - j]
# )

