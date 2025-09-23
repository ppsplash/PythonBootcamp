programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
print(f"student_scores: {student_scores}")
student_grades = {}  # my code- i created an empty dictionary , updated the values in student_scores and merged the values to student_grades
for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_scores[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_scores[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_scores[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_scores[key] = "Fail"
student_grades = student_grades | student_scores
print(f"student_grades: {student_grades}")

""" - my instructor code
student_grades={}
# Loop through each key in the student_scores dictionary
for student in student_scores:

    # Get the value (student score) by using the key each time.
    score = student_scores[student]

    # Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
print(student_grades)"""
