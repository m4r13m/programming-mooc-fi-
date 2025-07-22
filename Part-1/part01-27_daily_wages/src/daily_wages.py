hourly_wage = float(input("Hourly wage:"))
hours_worked = int(input("Hours worked: "))
day = input("Day")
wage = hourly_wage * hours_worked
if day == "Sunday":
    wage *= 2

print(f"Daily wages: {wage} euros")