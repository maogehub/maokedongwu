import unittest
import relocate

class RelocateTest(unittest.TestCase):
    def test_relocate(self):
        self.assertEqual(relocate.move(None, None), None, 'test relocate')