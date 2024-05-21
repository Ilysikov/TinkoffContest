from unittest import TestCase, main
from eight import eight


class eight_test(TestCase):
    def test_1(self):
        self.assertEqual(eight(one_string=[10, 5], two_string=[3.0, 2.5, 1.0, 2.5, 1.0, 1.5, 3.0, 1.5]),
                         (2.5, 2.0833333333333335))

    def test_2(self):
        self.assertEqual(eight(one_string=[10, 5], two_string=[6.0, 3.0, 8.0, 3.0, 8.0, 2.0, 6.0, 2.0]),
                         (7.5, 2.5))

    def test_3(self):
        self.assertEqual(eight(one_string=[10, 5], two_string=[2.0, 1.0, 1.0, 1.0, 1.0, 3.0, 2.0, 3.0]),
                         (1.8181818181818181, 1.6666666666666667))


if __name__ == '__main__':
    main()
