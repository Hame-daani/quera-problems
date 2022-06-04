import unittest
import sys
sys.path.append('../Initial_project')

class TestEsmFamil(unittest.TestCase):
    def _makeOne(self, clear=False):
        if clear:
            try:
                del sys.modules['source']
            except KeyError:
                pass
        import source
        return source

    def test_sample1(self):
        cur = self._makeOne(clear = True)
        cur.ready_up()
        cur.add_participant(participant = 'salib',
                            answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش',
                                       'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
        cur.add_participant(participant = 'kianoush',
                            answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی',
                                       'ashia': 'بیل', 'ghaza': 'به   پلو'})
        cur.add_participant(participant = 'sajjad',
                            answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ',
                                       'ashia': '        ', 'ghaza': 'برنج خورشت'})
        cur.add_participant(participant = 'farhad',
                            answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ',
                                       'ashia': 'بیل', 'ghaza': 'باقلوا'})
        self.assertDictEqual(cur.calculate_all(), {'salib': 65, 'kianoush': 55, 'sajjad': 45, 'farhad': 40})

    def test_sample2(self):
        cur = self._makeOne(clear = True)
        cur.ready_up()
        cur.add_participant(participant = 'salib',
                            answers = {'esm': 'ایدا', 'famil': 'اسدی', 'keshvar': 'المان', 'rang': 'ابی',
                                       'ashia': 'اره', 'ghaza': 'اش'})
        cur.add_participant(participant = 'kianoush',
                            answers = {'esm': 'امیر', 'famil': 'اکبری', 'keshvar': 'انگولا', 'rang': 'اجری',
                                       'ashia': 'اره برقی', 'ghaza': 'اب گوشت'})
        cur.add_participant(participant = 'sajjad',
                            answers = {'esm': 'ارمان', 'famil': 'ارمانی', 'keshvar': 'ایتالیا', 'rang': 'ارغوانی',
                                       'ashia': 'اب پاش', 'ghaza': 'اب گوشت'})
        cur.add_participant(participant = 'ali',
                            answers = {'esm': 'ارش', 'famil': 'اعظمی', 'keshvar': 'ارژانتین', 'rang': 'ارکیده',
                                       'ashia': 'ایینه', 'ghaza': 'اب گوشت'})
        cur.add_participant(participant = 'mamad',
                            answers = {'esm': 'امنه', 'famil': 'ازادی', 'keshvar': 'ارمنستان', 'rang': 'البالویی',
                                       'ashia': 'استکان', 'ghaza': 'اب گوشت'})
        self.assertDictEqual(cur.calculate_all(), {'salib': 60, 'kianoush': 55, 'sajjad': 55, 'ali': 55, 'mamad': 55})


if __name__ == '__main__':
    unittest.main()
