import unittest
import sys
sys.path.append('../Initial_project')
from security import Security

class ScoreListTest(unittest.TestCase):

    def test_encrypt_method_1(self):
        sec = Security()
        self.assertEqual("", sec.encrypt(""))

    def test_encrypt_method_2(self):
        sec = Security()
        self.assertEqual("4812162024", sec.encrypt("dddddd"))


    def test_is_social_account_info_method_1(self):
        sec = Security()
        self.assertEqual(False, sec.is_social_account_info("www.imdb.com"))

    def test_is_social_account_info_method_2(self):
        sec = Security()
        self.assertEqual(False, sec.is_social_account_info("imdb:www.imdb.com/account"))

    def test_secure_method_1(self):
        sec = Security()
        param = "Tell me something boy? Are You Happy in this modern world? Or do you need more?"
        excp = "Tell me something boy? Are You Happy in this modern world? Or do you need more?"
        self.assertEqual(excp, sec.secure(param))
        
        
if __name__ == '__main__':
    unittest.main()