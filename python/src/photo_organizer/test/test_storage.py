import unittest
import os

import storage

class StorageEngine(unittest.TestCase):
    """test storage engin
    """
    def setUp(self):
        self.db='.unittest.storage.engine.db'
        self.storage = storage.Storage(self.db)

    def test_insert(self):
        """test insert and insert duplicate
        """
        self.assertFalse(self.storage.has_key('test','me'), 'insert value')
        self.assertTrue(self.storage.has_key('test','me'), 'insert duplicate')

    def test_delete_key(self):
        """test delete (by name, by data and by both) or None
        """
        self.storage.has_key('test', 'me')
        self.assertTrue( self.storage.remove_key(data='me'), 'delete record by data')
        self.assertFalse( self.storage.has_key('test', 'me'), 'insert after delete')
        self.assertTrue( self.storage.remove_key('test', 'me'), 'delete record by name and data')
        self.assertFalse( self.storage.has_key('test', 'me'), 'insert after delete by name and data')
        self.assertTrue(self.storage.remove_key("test"), 'delete record by name')
        self.assertFalse( self.storage.has_key('test', 'me'), 'insert after delete by name')
        self.assertEquals( self.storage.remove_key(), None, 'delete record with None name and None data')
        
    def test_fetch_key(self):
        """test fetch key by name, data and both or None
        """
        self.storage.has_key('test', 'me')
        self.assertEqual(self.storage.fetch_key(), None, 'fetch key with None name and None value')
        self.assertEqual(self.storage.fetch_key('test')[0], ('test', 'me'), 'fetch key  by name')
        self.assertEqual(self.storage.fetch_key('test', data = 'me')[0], ('test', 'me'), 'fetch key  by name and data')
        self.assertEqual(self.storage.fetch_key(data = 'me')[0], ('test', 'me'), 'fetch key  by data')

    def test_add_metadata(self):
        """test add metadata and add duplicate
        """
        self.assertTrue(self.storage.add_metadata('test', 'me'), 'add metadata')
        self.assertFalse(self.storage.add_metadata('test', 'me'), 'add metadata duplicate on name and value')
        self.assertTrue(self.storage.add_metadata('test2', 'me'), 'add metadata different name duplicate value')
        self.assertFalse(self.storage.add_metadata('test', 'me2'), 'add metadata duplicate name different value')

    def test_remove_metadata(self):
        """test remove metadata by name, data or both or None
        """
        self.storage.add_metadata('test', 'me')
        self.assertTrue(self.storage.remove_metadata(name='test'), 'delete record by name')
        self.assertTrue(self.storage.add_metadata('test', 'me'))

    def test_remove_metadata_by_name_value(self):
        """test remove metadata by metadata's name and value
        """
        self.storage.add_metadata('test', 'me')
        self.assertTrue(self.storage.remove_metadata('test', 'me'), 'remove date with name and data')
        self.assertTrue(self.storage.add_metadata('test', 'me'), 'add data after remove')
        self.assertEqual(self.storage.remove_metadata(), None, 'remove with None medatada')
        self.assertTrue(self.storage.remove_metadata(data = 'me'), 'remove metadata with data')

    def test_fetch_metadata(self):
        """test fetch metadata
        """
        self.storage.add_metadata('test', 'me')
        self.assertEqual( self.storage.fetch_metadata('test')[0], ('test', 'me'), 'fetch metadata by name and data')
        self.assertEqual( self.storage.fetch_metadata(data='me')[0], ('test', 'me'), 'fetch metadata by data')
        self.assertEqual( self.storage.fetch_metadata(name='test', data='me')[0], ('test', 'me'), 'fetch metadata by name and value')
        self.assertEqual( self.storage.fetch_metadata(), None, 'fetch metadata by name=None and data=None')


    def tearDown(self):
        self.storage.close()
        os.remove(self.db)
