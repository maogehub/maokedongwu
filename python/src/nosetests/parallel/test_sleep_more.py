import time
import unittest

class Sleep(unittest.TestCase):
    def test_sleep6(self):
        time.sleep(6)
        self.assertTrue(1, 1)
