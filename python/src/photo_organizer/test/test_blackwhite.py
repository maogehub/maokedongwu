import unittest
import os
import blackwhite

class BlackWhite(unittest.TestCase):
    """test if the photo is black and white
    """    
    
    def test_blackwhite(self):
        color = os.path.join(os.path.dirname(__file__), 'data/exif.jpg')
        black = os.path.join(os.path.dirname(__file__), 'data/blackwhite.jpg')
        
        self.assertTrue(blackwhite.isblack(black), 'photo is black')
        self.assertFalse(blackwhite.isblack(color), 'photo is black')