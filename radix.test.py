import unittest
from radix import convert_number, num_closed_spaces


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

    def test_num_closed_spaces(self):
        tests = [
            ['489', 4],
            ['1001', 2],
            ['2AF', 1],
        ]

        for [num_str, expected] in tests:
            with self.subTest(msg=f'num_str: {num_str}'):
                self.assertEqual(num_closed_spaces(num_str), expected)


if __name__ == '__main__':
    unittest.main()

