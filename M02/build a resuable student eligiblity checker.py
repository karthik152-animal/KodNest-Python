def check_eligibility(marks, attendance, project_completed):
    if marks < 60:
        return "Not Eligible"
    elif attendance < 75:
        return "Not Eligible"
    elif project_completed != "yes":
        return "Not Eligible"
    else:
        return "Eligible"

marks = int(input())
attendance = int(input())
project_completed = input().strip().lower()

result = check_eligibility(marks, attendance, project_completed)
print(result)