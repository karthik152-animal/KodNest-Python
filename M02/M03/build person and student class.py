class Person:
    def display_name(self, name):
        print(f"Student Name: {name}")


class Student(Person):
    pass


name = input().strip()

student = Student()
student.display_name(name)