# Copy here code of line function from previous exercise
def line(n, char):
    if char == "":
        print("*" * n)
    else:
        print(char[0] * n)

def square_of_hashes(size):
    i = 0
    while i < size:
    # You should call function line here with proper parameters
        line(size, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
