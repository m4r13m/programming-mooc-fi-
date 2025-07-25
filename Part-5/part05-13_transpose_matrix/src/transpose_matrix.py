def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Iterate only for upper triangle to avoid double swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

 

if __name__ == "__main__":
    print(transpose([[1,2,3],[88,41,6],[6,10,777]]))