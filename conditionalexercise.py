from doctest import Example


Marios_exam_score = int(input("Enter your mark"))
Mario_entered_the_exam = True

if Marios_exam_score > 85 and Mario_entered_the_exam:
    print("Distinction")
elif Marios_exam_score >= 65 <= 85 and Mario_entered_the_exam:
    print("Pass")
else:
    print("Fail")