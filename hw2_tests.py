from wsgiref.validate import assert_

import data
import hw2
import unittest
class TestCases(unittest.TestCase):

# Write your test cases for each part below.

    # Part 1
    def test_create_rectangle_1(self):
        p1 = data.Point(2,1)
        p2 = data.Point(1,2)
        result = hw2.create_rectangle(p1,p2)
        expected = data.Rectangle(data.Point(2,1),data.Point(1,2))
        self.assertEqual(expected, result)
    def test_create_rectangle_2(self):
        p1 = data.Point(3,1)
        p2 = data.Point(1,3)
        result = hw2.create_rectangle(p1,p2)
        expected = data.Rectangle(data.Point(3,1),data.Point(1,3))
        self.assertEqual(expected, result)
    # Part 2
    # def test_shorter_duration_than(self):
    def test_shorter_than_duration_1(self):
        duration1 = "1:33:00"
        duration2 = "2:00:00"
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)
    def test_shorter_than_duration_2(self):
        duration1 = "2:33:00"
        duration2 = "2:00:00"
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(expected, result)
    # Part 3
    def test_duration_in_seconds_1(self):
        data.Duration = "4:00"
        result = hw2.duration_in_seconds(data.Duration)
        expected = 240
        self.assertEqual(expected, result)
    def test_duration_in_seconds_2(self):
        data.Duration = "5:00"
        result = hw2.duration_in_seconds(data.Duration)
        expected = 300
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time_1(self):
        running_time = [0,1,2,3]
        result = running_time
        expected = 6
        self.assertEqual(expected, result)
    def test_running_time_2(self):
        running_time = [0,1,2,4]
        result = running_time
        expected = 7
        self.assertEqual(expected, result)
    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
