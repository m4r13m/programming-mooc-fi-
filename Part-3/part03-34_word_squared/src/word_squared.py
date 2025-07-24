def squared(sub, n):
    s = sub * n * n
    i = 0
    j = 0
    while i < n:
        print(s[j: j+n])
        i += 1
        j += n

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)