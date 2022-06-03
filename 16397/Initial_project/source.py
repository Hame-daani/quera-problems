class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = int(stu_id)
        self.course_code = int(crc_code)
        self.score = float(score)


class CourseUtil:
    def set_file(self, address):
        self.file = address
        self.load_all()

    def load_all(self):
        with open(self.file, "r") as f:
            lines = f.readlines()
            self.all_grades = [Grade(*line.strip("\n").split(" ")) for line in lines]

    def load(self, line_number):
        return self.all_grades[line_number - 1]

    def calc_student_average(self, student_id):
        std_grades = [g.score for g in self.all_grades if g.student_id == student_id]
        return sum(std_grades) / len(std_grades)

    def calc_course_average(self, course_code):
        course_grades = [
            g.score for g in self.all_grades if g.course_code == course_code
        ]
        return sum(course_grades) / len(course_grades)

    def count(self):
        return len(self.all_grades)

    def save(self, grade: Grade):
        for g in self.all_grades:
            if grade.student_id == g.student_id and grade.course_code == g.course_code:
                return
        with open(self.file, "a") as f:
            f.write(f"\n{grade.student_id} {grade.course_code} {grade.score}")
        self.load_all()
