def oldest_person(people: list):
    old = people[0][1]
    for person in people:
        if person[1] < old:
            old = person[1]
    for p in people:
        if p[1] == old:
            return p[0]
        

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))