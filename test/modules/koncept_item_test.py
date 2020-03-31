import os, unittest
from src.modules.koncept_item import KonceptItem
from test.definitions import root


class KoceptItemTest(unittest.TestCase):
    
    def setUp(self):
        self.dbfile = os.path.join(root, 'db/item.csv')

    def tearDown(self):
        if os.path.exists(self.dbfile):
            os.remove(self.dbfile)

    def test_save_should_write_db(self):
        item = KonceptItem(self.dbfile)
        item.save(1, 'spoons', 1000)

        with open(self.dbfile, 'r') as db:
            content = db.readlines()
            self.assertEqual(content, ['1, spoons, 1000\n'])

    def test_delete_should_delete_item_from_db(self):
        item = KonceptItem(self.dbfile)
        item.save(1, 'spoons', 1000)
        item.delete('spoons')

        with open(self.dbfile, 'r') as db:
            content = db.readlines()
            self.assertEqual(content, [])

    def test_delete_should_delete_the_correct_item_from_db(self):
        item = KonceptItem(self.dbfile)
        item.save(1, 'spoons', 1000)
        item.save(2, 'forks', 1000)

        with open(self.dbfile, 'r') as db:
            content = db.readlines()
            self.assertEqual(content, ['1, spoons, 1000\n', '2, forks, 1000\n'])

        item.delete('spoons')

        with open(self.dbfile, 'r') as db:
            content = db.readlines()
            self.assertEqual(content, ['2, forks, 1000\n'])
    
    def test_search_shoud_return_the_item(self):
        item = KonceptItem(self.dbfile)
        item.save(1, 'spoons', 1000)

        self.assertEqual(['1, spoons, 1000\n'], item.search('spoons'))

    def test_search_shoud_return_the_correct_item(self):
        item = KonceptItem(self.dbfile)
        item.save(1, 'spoons', 1000)
        item.save(2, 'forks', 1000)

        self.assertEqual(['1, spoons, 1000\n'], item.search('spoons'))
if __name__ == '__main__':
    unittest.main()