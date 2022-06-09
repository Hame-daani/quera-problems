from unittest import TestCase
import unittest

from logger import logger
import sys
sys.path.append('../Initial_project')
from pyranj import PyRanj

ARG = 'arg'
KWARG = 'kwarg'


def pyranj_message(e, prefix=None):
    if prefix is None:
        prefix = '[EXCEPTION]'
    return f'{prefix} :: {e}'


def func(*args, **kwargs):
    return f'args={args}, kwargs={kwargs}'


def error_func(*args, **kwargs):
    raise Exception(f'args={args}, kwargs={kwargs}')


class BasePyRanjTest(TestCase):
    def setUp(self):
        logger.flush()
        self.prefix = None
        self.pyranj = PyRanj

    def wrapper_pass(self, wrapper):
        @wrapper
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)

        self.assertEqual(func(ARG, kwarg=KWARG), wrapped_func(ARG, kwarg=KWARG))

    def wrapper_error(self, wrapper):
        @wrapper
        def wrapped_func(*args, **kwargs):
            return error_func(*args, **kwargs)

        messages = []
        try:
            error_func(ARG, kwarg=KWARG)
        except Exception as e:
            messages.append(pyranj_message(e, prefix=self.prefix))

        wrapped_func(ARG, kwarg=KWARG)

        self.assertEqual(messages, logger.messages)

    def context_pass(self, context):
        messages = []

        with context:
            messages.append('SUCCESS')

        self.assertEqual(messages, ['SUCCESS'])

    def context_error(self, context):
        with context:
            raise Exception('x')

        self.assertEqual(logger.messages, [pyranj_message(Exception('x'), prefix=self.prefix)])

    def extension_pass(self, parent):
        class A(parent):
            def run(slf, *args, **kwargs):
                return func(*args, **kwargs)

        self.assertEqual(func(ARG, kwarg=KWARG), A().run(ARG, kwarg=KWARG))

    def extension_error(self, parent):
        class A(parent):
            def run(slf, *args, **kwargs):
                return error_func(*args, **kwargs)

        messages = []
        try:
            error_func(ARG, kwarg=KWARG)
        except Exception as e:
            messages.append(pyranj_message(e, prefix=self.prefix))

        A().run(ARG, kwarg=KWARG)

        self.assertEqual(messages, logger.messages)

    def test_wrapper(self):
        self.wrapper_pass(self.pyranj)
        self.wrapper_error(self.pyranj)

    def test_context(self):
        self.context_pass(self.pyranj)
        self.context_error(self.pyranj)

    def test_extension(self):
        self.extension_pass(self.pyranj)
        self.extension_error(self.pyranj)


if __name__ == '__main__':
    unittest.main()