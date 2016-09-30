# From the exercise, Student Becomes the Teacher

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return .1 * homework + .3 * quizzes + .6 * tests # relative weighting

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print "lloyd: " + get_letter_grade(get_average(lloyd))
print "alice: " + get_letter_grade(get_average(alice))
print "tyler: " + get_letter_grade(get_average(tyler))
print "tyler avg. hw score: " + str(average(tyler["homework"]))
print "tyler avg. quiz score: " + str(average(tyler["quizzes"]))
print "tyler avg. test score: " + str(average(tyler["tests"]))
# damn tyler, do your freakin hw and show up for quizzes

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

students = [lloyd, alice, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))