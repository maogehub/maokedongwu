import unittest
import os
import checksum

class Md5Test(unittest.TestCase):
    """test md5 module
    """
    def setUp(self):
        self.target = '.unittest.md5'
        self.md5 = '098f6bcd4621d373cade4e832627b4f6'
        open(self.target, 'w').write("test")


    def test_md5(self):
        """test md5 checksum
        """
        self.assertEqual(checksum.md5(self.target), self.md5, 'md5 checksum')
        os.chmod(self.target, 0)
        self.assertEqual(checksum.md5(self.target), None, 'file access check')

    def tearDown(self):
        os.remove(self.target)
