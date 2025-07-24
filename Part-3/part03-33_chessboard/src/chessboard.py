def chessboard(n):
    j = n // 2
    if n % 2 == 0:
        i = 0
        while i < n:
            if i % 2 == 0:
                print("10" * j)
            else:
                print("01" * j)
            i += 1
    else:
        i = 0
        while i < n:
            if i % 2 == 0:
                print("10" * (j) + "1")
            else:
                print("01" * (j) + "0")
            i += 1
        
# Testing the function
if __name__ == "__main__":
    chessboard(3)
