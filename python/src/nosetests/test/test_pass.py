import unittest
import sys
import logging

class TestPass(unittest.TestCase):
    def test_pass(self):
        print "stdout: xxx"
        print >>sys.stderr, ("stderr: yyyy")
        logging.info("info log")
        logging.debug("debug log")
        self.assertEqual(1, 1, '1=1')

