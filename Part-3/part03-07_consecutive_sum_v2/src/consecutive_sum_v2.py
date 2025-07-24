limit = int(input("Limit: "))
sentence = ""
s = 0
i = 1
while s < limit:
    s += i
    if s < limit:
        sentence += f"{i} + "
    else:
        sentence += f"{i}"
    i += 1

print(f"The consecutive sum: {sentence} = {s}")