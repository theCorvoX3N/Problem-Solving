n = int(input().strip())
grades = []

def round_grades(original_grades):
    for each in range(len(original_grades)):
        rem = original_grades[each]%5
        if (rem >= 3) and (original_grades[each]>=38):
            original_grades[each] += (5-rem)

for grades_i in range(n):
    grades_t  = int(input().strip())
    grades.append(grades_t)

round_grades(grades)

for each in grades:
    print(each)
