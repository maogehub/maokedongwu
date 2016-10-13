import unittest
import os
from lib import exif

class Exif(unittest.TestCase):
    """test exif read
    """

    def test_read(self):
        """test exif from example photo
        """
        sample = {
            'YResolution': -0.6666666666666666,
            'ExifTag': 90L,
            'XResolution': -2L,
            'DateTimeOriginal': 978325199.0,
            'Model': 'Test 1',
            'SamplesPerPixel': 162}
        #pycharm running test is different than running nosetests from shell, hack the path
        filename = os.path.join(os.path.dirname(__file__), 'data/exif.jpg')
        self.assertEqual(exif.get(filename), sample, 'exif read test')
        self.assertEqual(exif.get('do_not_exist'), {}, 'exif read without os.R_OK')

