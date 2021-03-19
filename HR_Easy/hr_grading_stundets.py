''' 
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
''' 
import math


grades = [4, 73, 67, 38, 33]


def grading_studnets(grades):
    final_grade = []
    next_multiple = 0
    for grade in grades:
        next_multiple = 5 * math.ceil(grade/5)
        if next_multiple - grade < 3 and next_multiple >= 40:
            print(f'{next_multiple} - {grade} = {abs(next_multiple - grade)}')
            final_grade.append(next_multiple)
        else:
            final_grade.append(grade)

    return final_grade


if __name__ == '__main__':
    print(grading_studnets(grades))