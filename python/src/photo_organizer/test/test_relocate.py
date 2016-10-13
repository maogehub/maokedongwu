import unittest
import os
import relocate
import re
import shutil

class RelocateTest(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.jpg'
        self.path = '.unittest_relocate'
        self.time = {
            'epoch': '1476325378.0',
            'path': '2016/10/13'}
        
    def test_relocate(self):
        
        open(self.filename, 'w').write('')
        test = (self.filename, self.time['epoch'])
        self.assertEqual(relocate.move(test, self.path), None, 'move file to target')
        self.assertTrue(os.path.isfile('%s/%s/%s' % (self.path, self.time['path'], self.filename)), 'verify file in target')
        open(self.filename, 'w').write('')
        self.assertEqual(relocate.move(test, self.path), None, 'move duplicate file to target')
        for f in os.listdir('%s/%s' % (self.path, self.time['path'])):
            m = re.match(r'uuid-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4,}-[0-9a-f]{12}-%s' % self.filename, f)
            if m:
                break
        self.assertTrue(m, 'verify duplicated file in target as uuid-UUID.UUID4-filename')
        
    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)            
        if os.path.isdir(self.path):        
            shutil.rmtree(self.path)