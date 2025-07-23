year = int(input("Year:"))
if (year % 4 == 0 and year%100 != 0) or (year%100 == 0 and year% 400==0):
    y = year + 4
    while True:
        if(y % 4 == 0 and y%100 != 0) or (y%100 == 0 and y% 400==0):
            break
        y += 4
    print(f"The next leap year after {year} is {y}")
else:
    yy = year + 1
    while True:
        if(yy % 4 == 0 and yy%100 != 0) or (yy%100 == 0 and yy% 400==0):
            break
        yy += 1
    print(f"The next leap year after {year} is {yy}")