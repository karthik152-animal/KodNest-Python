import JavaDeveloper
class Developer:
    def work(self):
        print("Developer is working")

    def attendMeeting(self):
        print("Developer is attending meeting")

class JavaDeveloper(Developer):
    def work(self):
        print("Java Developer is working on java")

    def doJavaproject(self)
        print("Java Developer is building a java project")

class PythonDeveloper(Developer):
    def work(self):
        print("Python Developer is working on python")
    def doPythonProject(self):
        print("Python Developer is building a python project")

dev = Developer()
dev.work()
dev.attendMeeting()
