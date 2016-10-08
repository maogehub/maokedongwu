import unittest
import sys
import logging

class TestSkip(unittest.TestCase):
    @unittest.skip("skip this test")
    def test_skip(self):
        print "stdout: xxx skip"
        print >>sys.stderr, ("stderr: yyyy skip")
        logging.info("info log skip")
        logging.debug("debug log skip")
        self.assertEqual(1, 1, '1=1')

