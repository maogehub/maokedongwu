#!/usr/bin/python
import cache
import unittest
import time

class TestCache(unittest.TestCase):

    def test_cache(self):
        """test cache
        """
        @cache.Cache()
        def return_value():
            return time.time()
        value=return_value()
        self.assertEqual(value, return_value())

    def test_cache_passthrough(self):
        """test cache pass through
        """
        @cache.Cache()
        def return_value(value):
            return time.time()
        value=return_value(0)
        self.assertNotEqual(value, return_value(1))

    def test_cache_timeout(self):
        """test cache time out
        """
        @cache.Cache(timeout=1)
        def return_value(value):
            return time.time()
        value=return_value(0)
        time.sleep(2)
        self.assertNotEqual(value, return_value(0))

