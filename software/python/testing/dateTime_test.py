import sys, os, json
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from date_timeHandler import getDayFromDateTime, getHourFromDateTime, getMinuteFromDateTime
import unittest


date = "2024-05-13 09:20:45.574018"

class date_time_test(unittest.TestCase):
    def test_day(self):
        self.assertEqual(getDayFromDateTime(date), "2024-05-13")
        
    def test_hour(self):
        self.assertEqual(getHourFromDateTime(date), "09:00")
        
    def test_minute(self):
        self.assertEqual(getMinuteFromDateTime(date), "09:20")

if __name__ == "__main__":
    unittest.main()