"""Unit tests for schedule.py"""
import datetime
import functools
import mock
import unittest
import sys
sys.path.append('../Initial_project')
# Silence "missing docstring", "method could be a function",
# "class already defined", and "too many public methods" messages:
# pylint: disable-msg=R0201,C0111,E0102,R0904,R0901

import schedule
from schedule import every


def make_mock_job(name=None):
    job = mock.Mock()
    job.__name__ = name or 'job'
    return job


class mock_datetime(object):
    """
    Monkey-patch datetime for predictable results
    """

    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def __enter__(self):
        class MockDate(datetime.datetime):
            @classmethod
            def today(cls):
                return cls(self.year, self.month, self.day)

            @classmethod
            def now(cls):
                return cls(self.year, self.month, self.day,
                           self.hour, self.minute)

        self.original_datetime = datetime.datetime
        datetime.datetime = MockDate

    def __exit__(self, *args, **kwargs):
        datetime.datetime = self.original_datetime


class SchedulerTests2(unittest.TestCase):
    def setUp(self):
        schedule.clear()

    def test_time_range(self):
        with mock_datetime(2014, 6, 28, 12, 0):
            mock_job = make_mock_job()

            # Choose a sample size large enough that it's unlikely the
            # same value will be chosen each time.
            minutes = set([
                every(5).to(30).minutes.do(mock_job).next_run.minute
                for i in range(100)
            ])

            assert len(minutes) > 1
            assert min(minutes) >= 30
            assert max(minutes) <= 35

    def test_time_range_repr(self):
        mock_job = make_mock_job()

        with mock_datetime(2014, 6, 28, 12, 0):
            job_repr = repr(every(5).to(30).minutes.do(mock_job))

        assert job_repr.startswith('Har 30 to 35 minutes do job()')
        
        

if __name__ == '__main__':
    unittest.main()