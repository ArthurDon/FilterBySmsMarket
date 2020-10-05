import unittest
import datetime
from utils import dates


class TestDates(unittest.TestCase):
    def test_old_date_expired(self):
        expected = True
        offset, max_duration = 0, 2
        old_date = datetime.datetime.now() - datetime.timedelta(minutes=max_duration)
        received = dates.is_expired(old_date, offset)        
        self.assertEqual(expected, received) 


    def test_future_date_not_expired(self):
        expected = False
        offset, max_duration = 0, -10
        future_date = datetime.datetime.now() - datetime.timedelta(minutes=max_duration)
        received = dates.is_expired(future_date, offset)        
        self.assertEqual(expected, received) 

    
    def test_current_date_not_expired(self):
        expected = False
        offset, max_duration = 0, 0
        future_date = datetime.datetime.now() - datetime.timedelta(minutes=max_duration)
        received = dates.is_expired(future_date, offset)        
        self.assertEqual(expected, received) 


