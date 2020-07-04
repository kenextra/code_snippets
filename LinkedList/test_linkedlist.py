import unittest
from linked_list import LinkedList, LLNode


class TestLLNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emypty_list = LinkedList()

    def test_get(self):
        with self.assertRaises(Exception):
            self.emypty_list.get(0)

        self.emypty_list.add_first(LLNode('kene'))

        with self.assertRaises(IndexError):
            self.emypty_list.get(-1)
            self.emypty_list.get(1)

    # def test_add_at(self):


if __name__ == '__main__':
    unittest.main()
