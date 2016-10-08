import time
import unittest

class Sleep(unittest.TestCase):
    def test_sleep5(self):
        time.sleep(5)
        self.assertTrue(1, 1)
