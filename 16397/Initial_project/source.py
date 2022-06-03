class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def set_file(self, address):
        pass

    def load(self, line_number):
        pass

    def calc_student_average(self, student_id):
        pass

    def calc_course_average(self, course_code):
        pass

    def count(self):
        pass

    def save(self, grade):
        pass