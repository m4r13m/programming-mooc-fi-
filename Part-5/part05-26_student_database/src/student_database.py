# adding students
def add_student(students, name):
    students[name] = ["no completed courses"]

# adding completed courses
def add_course(students, name, course):

    if course[1] != 0:
        if len(students[name]) == 1:
            students[name].append(course)
        else:
            for c in students[name][1:]:
                if c[0] == course[0] and c[1] < course[1]:
                    students[name].append(course)
                    students[name].remove(c)
                    return
                elif c[0] == course[0] and c[1] >= course[1]:
                    return
            students[name].append(course)
        


def print_student(students, name):
    grades = []
    if name not in students:
        print(f"{name}: no such person in the database")   

    else:
        if len(students[name]) == 1:
            print(name + ":")
            print(" no completed courses")

        else:
            print(name + ":")
            print(f" {len(students[name]) - 1} completed courses:")
            for course in students[name][1:]:
                print(f"  {course[0]} {course[1]}")
                grades.append(course[1])
            print(f" average grade {sum(grades) / len(grades)}")
            



def summary(students):
    number_students = 0
    best_average = 0
    most_course = 0
    q = ""
    p = ""
    for name in students:
        number_students += 1
        if most_course < len(students[name]) - 1:
            most_course = len(students[name]) - 1
            q = name
        total = 0
        for course in students[name][1:]:
            total += course[1]

        if best_average < total / (len(students[name]) - 1):
            best_average = total / (len(students[name]) - 1 )
            p = name

    print(f"students {number_students}") 
    print(f"most courses completed {most_course} {q}")
    print(f"best average grade {best_average} {p}")



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)



