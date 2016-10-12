import unittest
import blackwhite

class BlackWhite(unittest.TestCase):
    """test if the photo is black and white
    """    
    
    def test_blackwhite(self):
        self.assertTrue(blackwhite.isblack('xxx.jpg'), 'photo is black')