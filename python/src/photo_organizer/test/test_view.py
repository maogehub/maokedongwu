import unittest
from lib import view

class View(unittest.TestCase):
    def setUp(self):
        self.view = view.View()

    def test_view(self):
        self.assertTrue(self.view.some_view(), 'test some view')

    def tearDown(self):
        del self.view
