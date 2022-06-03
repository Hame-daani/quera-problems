import unittest
import sys
sys.path.append('../Initial_project')
from source import Grade, CourseUtil


class ScoreListTest(unittest.TestCase):
    def setUp(self):
        with open('sample_scores.txt', 'w') as fp:
            fp.write("123123123 123 12.5\n987987987 333 15\n123123123 333 17.8\n987987987 124 18.5")

    def _test_line(self, util, line_number, student_id, course_id, score):
        self.assertEqual(student_id, util.load(line_number).student_id)
        self.assertEqual(course_id, util.load(line_number).course_code)
        self.assertAlmostEqual(score, util.load(line_number).score, delta=1e-5)

    def _test_initial_data(self, util):
        self._test_line(util, 1, 123123123, 123, 12.5)
        self._test_line(util, 2, 987987987, 333, 15)
        self._test_line(util, 3, 123123123, 333, 17.8)
        self._test_line(util, 4, 987987987, 124, 18.5)

    def test_count(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        self.assertEqual(4, util.count())

    def test_load(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        self._test_initial_data(util)

    def test_save(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        score = Grade(123123123, 312, 19)
        util.save(score)
        self.assertEqual(5, util.count())
        self._test_initial_data(util)
        self._test_line(util, 5, 123123123, 312, 19)

    def test_save_and_set_file_after(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        score = Grade(123123123, 312, 19)
        util.save(score)
        self.assertEqual(5, util.count())
        self._test_initial_data(util)
        self._test_line(util, 5, 123123123, 312, 19)

        util.set_file('sample_scores.txt')

        self.assertEqual(5, util.count())
        self._test_initial_data(util)
        self._test_line(util, 5, 123123123, 312, 19)

    def test_save_duplicate_grade(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        score = Grade(123123123, 123, 12.5)
        util.save(score)
        self.assertEqual(4, util.count())
        self._test_initial_data(util)

    def test_calc_course_average(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        self.assertAlmostEqual(16.4, util.calc_course_average(333), delta=1e-5)

    def test_student_average(self):
        util = CourseUtil()
        util.set_file('sample_scores.txt')
        self.assertAlmostEqual(15.15, util.calc_student_average(123123123), delta=1e-5)
        

if __name__ == '__main__':
    unittest.main()