tf = int(input("Please type in a temperature (F): "))
tc = (tf - 32) * (5/9)
print(f"{tf} degrees Fahrenheit equals {tc} degrees Celsius")
if tc < 0:
    print("Brr! It's cold in here!")