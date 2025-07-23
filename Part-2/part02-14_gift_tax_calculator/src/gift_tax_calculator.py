v = int(input("Value of gift: "))
if v < 5000:
    print("No tax!")
elif 5000 <= v < 25000:
    tax = 100 + (v - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")
elif 25000 <= v < 55000:
    tax = 1700 + (v - 25000) * 0.1
    print(f"Amount of tax: {tax} euros")
elif 55000 <= v < 200000:
    tax = 4700 + (v - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")
elif 200000 <= v < 1000000:
    tax = 22100 + (v - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")
else:
    tax = 142100+ (v - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")