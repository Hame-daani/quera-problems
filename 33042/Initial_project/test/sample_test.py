from unittest import TestCase
import sys
import unittest

from numpy import unicode_
sys.path.append('../Initial_project')
from material import User, TrafficUsageDao, TrafficUsage
from service import TrafficUsageService

a100 = User('a100', 'Ali', 20)
a101 = User('a101', 'Hasan', 19)
a102 = User('a102', 'Mehri', 35)


class SampleTrafficUsageDao(TrafficUsageDao):
    def load_all(self):
        def generate_record_for_user(user, year, month, internal, daily, usage):
            return [
                TrafficUsage(user, internal, daily, usage, "" + str(year) + "/" + str(month) + "/" + str(j)) for j in range(0, 30)
            ]

        return [
            *generate_record_for_user(a100, 97, "01", False, False, 100),
            *generate_record_for_user(a100, 98, "02", False, True, 100),  # download lover
            *generate_record_for_user(a100, 98, "02", False, False, 90),

            *generate_record_for_user(a101, 97, "01", False, False, 100),
            *generate_record_for_user(a101, 98, "02", False, True, 100),
            *generate_record_for_user(a101, 98, "02", False, False, 100),

            *generate_record_for_user(a102, 97, "01", True, True, 200),
            *generate_record_for_user(a102, 97, "01", False, False, 120),
            *generate_record_for_user(a102, 98, "02", False, True, 120),
            *generate_record_for_user(a102, 98, "02", False, False, 120),
        ]


class TestTrafficUsageService(TestCase):
    def setUp(self):
        self.service = TrafficUsageService(SampleTrafficUsageDao())


    def test_social_media_lovers(self):
        self.assertCountEqual(
            self.service.social_media_lovers(96, 2),
            []
        )

    def test_download_lovers(self):
        self.assertCountEqual(
            self.service.download_lovers(97, 1),
            [a102]
        )
        
        
if __name__ == '__main__':
    unittest.main()