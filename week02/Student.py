# Student

class Student:
    def __init__(self, name, student_id, course):
        self._name = name
        self._student_id = student_id
        self._course = course
        self._mark = 0

    @property
    def name(self):
        return self._name
    @property
    def student_id(self):
        return self._student_id
    @property
    def course(self):
        return self._course
    @property
    def mark(self):
        return self._mark

    def study(self):
        print(f"{self._name} is studying")

    def update_mark(self, mark):
        if mark >=0 and mark <= 100:
            self._mark = mark
        else:
            print("Invalid mark - must be between 0 and 100")

def main():
    student = Student('', 1, 100)
    student.study()

if __name__ == '__main__':
    main()


