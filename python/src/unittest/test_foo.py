#!/usr/bin/python
"""
unittest for test foo.py
"""
import unittest
import foo
class TestFoo(unittest.TestCase):
    def setUp(self):
        self.foo=foo.Foo()
    def tearDown(self):
        del self.foo
    def test_true(self):
        self.assertTrue(self.foo.return_true())
    def test_false(self):
        self.assertFalse(self.foo.return_false())
if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    unittest.TextTestRunner(verbosity=2).run(suite)
