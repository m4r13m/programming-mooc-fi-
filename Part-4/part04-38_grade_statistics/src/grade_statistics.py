exam_points = []
exercises_completed = []
exercise_points = []
while True:
    ex_ex = input("Exam points and exercises completed: ").strip()
    if ex_ex == "":
        break
    exam, exercise = ex_ex.split(" ")
    exam_points.append(int(exam))
    exercises_completed.append(int(exercise))


for ex in exercises_completed:
    exercise_points.append(ex // 10)

grades = []
total_points = []
for i in range(len(exam_points)):
    total_points.append(exam_points[i] + exercise_points[i])
    if exam_points[i] < 10:
        grades.append(0)
    else:
        grades.append(exam_points[i] + exercise_points[i])
    
g0 = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
for g in grades:
    if 0 <= g <= 14:
        g0 += 1
    elif 15 <= g <= 17:
        g1 += 1
    elif 18 <= g <= 20:
        g2 += 1
    elif 21 <= g <= 23:
        g3 += 1
    elif 24 <= g <= 27:
        g4 += 1
    elif 28 <= g <= 30:
        g5 += 1
gs = g0 + g1 + g2 + g3 + g4 + g5

points_average = sum(total_points) / len(total_points)
pass_percentage = 100 * (gs - g0) / gs

print("Statistics:")
print(f"Points average: {points_average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
print("  5: " + g5 * "*")
print("  4: " + g4 * "*")
print("  3: " + g3 * "*")
print("  2: " + g2 * "*")
print("  1: " + g1 * "*")
print("  0: " + g0 * "*")