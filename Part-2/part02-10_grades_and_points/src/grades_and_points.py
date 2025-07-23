p = int(input("How many points [0-100]:"))
if p <0 or p > 100:
    print("Grade: impossible!")
elif 0 <= p < 50:
    print("Grade: fail")
elif 50 <= p < 60:
    print("Grade: 1")
elif 60 <= p < 70:
    print("Grade: 2")
elif 70 <= p < 80:
    print("Grade: 3")
elif 80 <= p < 90:
    print("Grade: 4")
elif 90 <= p <= 100:
    print("Grade: 5")