import unittest, types
import sys
sys.path.append('../Initial_project')
from solution import ExceptionProxy, transform_exceptions


class ScoreListTest(unittest.TestCase):

    def test_normal(self):
        def f():
            1 / 0

        def g():
            int("salam")

        def h():
            "salam" + 1

        func_ls = [f, g, h]
        user_ls = transform_exceptions(func_ls)
        self.assertEqual(len(user_ls), 3)

        self.assertEqual(True, isinstance(user_ls[0], ExceptionProxy))
        self.assertEqual(user_ls[0].msg, "division by zero")
        self.assertEqual(user_ls[0].function.__name__, "f")

        self.assertEqual(True, isinstance(user_ls[1], ExceptionProxy))
        self.assertEqual(user_ls[1].msg, "invalid literal for int() with base 10: 'salam'")
        self.assertEqual(user_ls[1].function.__name__, "g")

        self.assertEqual(True, isinstance(user_ls[2], ExceptionProxy))
        self.assertEqual(user_ls[2].msg, 'can only concatenate str (not "int") to str')
        self.assertEqual(user_ls[2].function.__name__, "h")

    def test_raised_exception(self):
        def f():
            raise NameError('salam')

        def g():
            raise ValueError

        def h():
            raise ZeroDivisionError

        func_ls = [f, g, f, f, g, h, f, h, g, g, h]
        user_ls = transform_exceptions(func_ls)

        self.assertEqual(len(user_ls), 11)
        self.assertEqual(True, isinstance(user_ls[0], ExceptionProxy))
        self.assertEqual(user_ls[0].msg, "salam")
        self.assertEqual(user_ls[0].function.__name__, "f")

        self.assertEqual(True, isinstance(user_ls[1], ExceptionProxy))
        self.assertEqual(user_ls[1].msg, "")
        self.assertEqual(user_ls[1].function.__name__, "g")

        self.assertEqual(True, isinstance(user_ls[2], ExceptionProxy))
        self.assertEqual(user_ls[2].msg, "salam")
        self.assertEqual(user_ls[2].function.__name__, "f")

        self.assertEqual(True, isinstance(user_ls[3], ExceptionProxy))
        self.assertEqual(user_ls[3].msg, "salam")
        self.assertEqual(user_ls[3].function.__name__, "f")

        self.assertEqual(True, isinstance(user_ls[4], ExceptionProxy))
        self.assertEqual(user_ls[4].msg, "")
        self.assertEqual(user_ls[4].function.__name__, "g")

        self.assertEqual(True, isinstance(user_ls[5], ExceptionProxy))
        self.assertEqual(user_ls[5].msg, "")
        self.assertEqual(user_ls[5].function.__name__, "h")

        self.assertEqual(True, isinstance(user_ls[6], ExceptionProxy))
        self.assertEqual(user_ls[6].msg, "salam")
        self.assertEqual(user_ls[6].function.__name__, "f")

        self.assertEqual(True, isinstance(user_ls[7], ExceptionProxy))
        self.assertEqual(user_ls[7].msg, "")
        self.assertEqual(user_ls[7].function.__name__, "h")

        self.assertEqual(True, isinstance(user_ls[8], ExceptionProxy))
        self.assertEqual(user_ls[8].msg, "")
        self.assertEqual(user_ls[8].function.__name__, "g")

        self.assertEqual(True, isinstance(user_ls[9], ExceptionProxy))
        self.assertEqual(user_ls[9].msg, "")
        self.assertEqual(user_ls[9].function.__name__, "g")

        self.assertEqual(True, isinstance(user_ls[10], ExceptionProxy))
        self.assertEqual(user_ls[10].msg, "")
        self.assertEqual(user_ls[10].function.__name__, "h")
        
        
if __name__ == '__main__':
    unittest.main()