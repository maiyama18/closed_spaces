import unittest
from radix import convert_number


class TestConvertNumber(unittest.TestCase):
    def test_convert_number(self):
        tests = [
            [10, 489, '489'],
            [2, 9, '1001'],
            [16, 687, '2AF'],
        ]

        for [radix, number, expected] in tests:
            with self.subTest(msg=f'radix: {radix}, number: {number}'):
                self.assertEqual(convert_number(number, radix), expected)


if __name__ == '__main__':
    unittest.main()
