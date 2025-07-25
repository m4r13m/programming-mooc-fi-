def count_matching_elements(matrix, n):
    m = 0
    for row in matrix:
        m += row.count(n)
    return m

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))