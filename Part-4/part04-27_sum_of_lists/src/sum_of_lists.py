def list_sum(x, y):
    s = []
    for i in range(len(x)):
        s.append(x[i] + y[i])
    return s

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]