import unittest
import sys
sys.path.append('../Initial_project')
from cube import coloring


class ScoreListTest(unittest.TestCase):

    def _check(self, l1, l2):
        if isinstance(l1, list):
            self.assertEqual(len(l1), len(l2))

            for i, j in zip(l1, l2):
                self._check(i, j)

        else:
            self.assertEqual(l1, l2)

    def _test(self, n, m, k):

        ls_user = [[[5 for i in range(k)] for j in range(m)] for it in range(n)]
        coloring(ls_user)
        ls_judge = [
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ]
        ]
        self._check(ls_user, ls_judge)

    def test(self):
        self._test(3, 3, 3)


if __name__ == '__main__':
    unittest.main()