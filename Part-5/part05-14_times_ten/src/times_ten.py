def times_ten(start_index: int, end_index: int):
    d = {}
    for i in range(start_index, end_index + 1):
        d[i] = i * 10
    return d


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)