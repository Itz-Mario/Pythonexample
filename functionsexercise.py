def IT_Grade(homework_score, assessment_score, final_exam_score):
    answer = (homework_score*assessment_score*final_exam_score)*100
    return "Your IT grade is: ", float(answer)


added_number = total_score = IT_Grade
print(added_number)


enter_name = input("Enter student name: ")
homework_score = int(input("Enter homework score /25: "))/25
assessment_score = int(input("Enter assessment score /50: "))/50
final_exam_score = int(input("Enter final exam score /100: "))/100

var1 = IT_Grade(homework_score, assessment_score, final_exam_score)
print(f"Your IT grade is:  {var1}")

