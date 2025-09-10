student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0 # without max() function
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

print(f"highest score is {max(student_scores)}") #can be done with fstring and max() function

sum_score= 0 #without sum() function
for score in student_scores:
    sum_score += score
print(sum_score)

print(f"the total score is {sum(student_scores)}") # with fstring and sum() function


