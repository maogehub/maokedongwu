import delete_raw_from_jpg
import os
import unittest
import re

class DeleteRawFromJPG(unittest.TestCase):
    def setUp(self):
        self.data = {
                'jpg': {
                    'path': '.jpg',
                    'files': ['1.jpg', '2.jpg'],
                    },
                'raw': {
                    'path': '.raw',
                    'files': ['2.raw', '3.raw'],
                    },
                }
        self.target='.test_delete'
        for i in self.data:
            if not os.path.isdir(self.data[i]['path']):
                os.mkdir(self.data[i]['path'])
            for f in self.data[i]['files']:
                open(os.path.join(self.data[i]['path'], f), 'w').write('')

    def test_delete(self):
        """check if we have raw but not jpg, then raw file deleted
        """
        delete_raw_from_jpg.delete_raw_from_jpg(self.data['jpg']['path'], self.data['raw']['path'], self.target)
        self.assertFalse(os.path.isfile(os.path.join(self.data['raw']['path'], '3.raw')))

    def test_unique(self):
        """check if files exist in target, we still have it in raw deleted (backed up)
        """
        if not os.path.isdir(self.target):
            os.mkdir(self.target)
        open(os.path.join(self.target, '3.raw'), 'w').write('')
        delete_raw_from_jpg.delete_raw_from_jpg(self.data['jpg']['path'], self.data['raw']['path'], self.target)
        for f in os.listdir(self.target):
            m = re.match(r'3\.raw-uuid-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4,}-[0-9a-f]{12}', f)
            if m:
                break
        self.assertTrue(m)

    def test_keep(self):
        """check if files exist in jpg, we still have it in raw
        """
        delete_raw_from_jpg.delete_raw_from_jpg(self.data['jpg']['path'], self.data['raw']['path'], self.target)
        self.assertTrue(os.path.isfile(os.path.join(self.data['raw']['path'], '2.raw')))


    def tearDown(self):
        for i in self.data:
            for f in os.listdir(self.data[i]['path']):
                os.remove(os.path.join(self.data[i]['path'], f))
            os.rmdir(self.data[i]['path'])
        if os.path.isdir(self.target):
            for f in os.listdir(self.target):
                os.remove(os.path.join(self.target, f))
            os.rmdir(self.target)
