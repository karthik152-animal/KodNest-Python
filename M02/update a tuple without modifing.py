course_name = input()
current_week = input()
course_status = input()

course_details = (course_name, current_week, course_status)

updated_week = input()

course_details = (course_details[0], updated_week, course_details[2])

print(course_details)