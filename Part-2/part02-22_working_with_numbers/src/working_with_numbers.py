c = 0
s = 0
ng = 0
np = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    n = int(input("Number:"))
    if n == 0:
        break
    c += 1
    s += n
    if n < 0:
        ng +=1
    else:
        np += 1
print(f"Numbers typed in {c}")
print(f"The sum of the numbers is {s}")
print(f"The mean of the numbers is {s/c}")
print(f"Positive numbers {np}")
print(f"Negative numbers {ng}")