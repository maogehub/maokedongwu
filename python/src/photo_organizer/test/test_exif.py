import unittest
import exif

class Exif(unittest.TestCase):
    def test_read(self):
        self.assertEqual(exif.get(None), None, 'exif read')