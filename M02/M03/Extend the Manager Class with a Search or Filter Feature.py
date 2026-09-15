class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student_profile(self, student_profile):
        self.students.append(student_profile)

    def filter_students_by_course(self, course):
        matched_students = [
            student for student in self.students 
            if student.course.lower() == course.lower()
        ]
        
        if matched_students:
            for student in matched_students:
                print(student)
        else:
            print(f"No students found for course: {course}")


if __name__ == "__main__":
    n = int(input().strip())
    manager = PlacementManager()

    for _ in range(n):
        student_id = input().strip()
        student_name = input().strip()
        course_name = input().strip()
        profile = StudentProfile(student_id, student_name, course_name)
        manager.add_student_profile(profile)

    target_course = input().strip()
    manager.filter_students_by_course(target_course)