def dict_of_numbers():
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 
        30:'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    j = 1
    for i in range(21, 30):
        d[i] = d[20] + "-" + d[j]
        j += 1
    j = 1
    for i in range(31, 40):
        d[i] = d[30] + "-" + d[j]
        j += 1
    j = 1
    for i in range(41, 50):
        d[i] = d[40] + "-" + d[j]
        j += 1
    j = 1
    for i in range(51, 60):
        d[i] = d[50] + "-" + d[j]
        j += 1
    j = 1
    for i in range(61, 70):
        d[i] = d[60] + "-" + d[j]
        j += 1
    j = 1
    for i in range(71, 80):
        d[i] = d[70] + "-" + d[j]
        j += 1
    j = 1
    for i in range(81, 90):
        d[i] = d[80] + "-" + d[j]
        j += 1
    j = 1
    for i in range(91, 100):
        d[i] = d[90] + "-" + d[j]
        j += 1

    return d

if __name__ =="__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])

