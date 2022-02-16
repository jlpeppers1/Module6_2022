import unittest
from main.area import area


class MyTestCase(unittest.TestCase):
    # naming standard must start with test_ to be tested during run
    # def test_*

    # define a standard test like this
    def test_area(self):
        expected = 2
        actual = area(1, 2)
        self.assertEqual(expected, actual)
        # can use different self.assert* function based on your needs

    def test_area_square(self):
        expected = 4
        actual = area(2)
        self.assertEqual(expected, actual)
        # can use different self.assert* function based on your needs

    # test an exception
    def test_exception_thrown(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area('alpha', 'bravo')

    def test_exception_negative(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area(-1, 4)

    def test_exception_negative_second(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area(1, -4)

    def test_exception_negative_both(self):
        # notice the with keyword, and the Error Type we are expecting
        with self.assertRaises(ValueError):
            area(-1, -4)

# driver, don't modify this
if __name__ == '__main__':
    unittest.main()
