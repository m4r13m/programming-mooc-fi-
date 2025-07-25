def factorials(n: int):
    f = {}
    i = 2
    f[1] = 1
    while i <= n:
        f[i] = f[i- 1] * i
        i += 1
    return f

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])