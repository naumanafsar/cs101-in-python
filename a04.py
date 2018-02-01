## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(grades):
    if round(grades >= 90):
        return "A+"
    if round(grades >= 86):
        return "A"
    if round(grades >= 82):
        return "A-"
    if round(grades >= 78):
        return "B+"
    if round(grades >= 74):
        return "B"
    if round(grades >= 70):
        return "B-"
    if round(grades >= 66):
        return "C+"
    if round(grades >= 62):
        return "C"
    if round(grades >= 58):
        return "C-"
    if round(grades >= 54):
        return "D+"
    if round(grades >= 50):
        return "D"
    else:
        return "F"


def f(points):
    if points == "A+":
        return 4.00
    if points == "A":
        return 4.00
    if points == "A-":
        return 3.67
    if points == "B+":
        return 3.33
    if points == "B":
        return 3.00
    if points == "B-":
        return 2.67
    if points == "C+":
        return 2.33
    if points == "C":
        return 2.00
    if points == "C-":
        return 1.67
    if points == "D+":
        return 1.33
    if points == "D":
        return 1.00
    if points == "F":
        return 0
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(grade1, grade2, grade3):
    total_marks = 0
    total_number_of_subjects = 0
    if grade1 != 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + f(grade1)
    if grade2 != 'nothing':
        total_number_of_subjects += 1
        total_marks = total_marks + f(grade2)
    if grade3 != 'nothing':
        total_number_of_subjects += 1
        total_marks = total_marks + f(grade3)


    if total_number_of_subjects == 0:
        return 0
    sgpa = total_marks/total_number_of_subjects
    return sgpa
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
