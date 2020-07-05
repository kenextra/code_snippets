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
        self.one_list = LinkedList(['first'])
        self.two_list = LinkedList(['second', 'third'])
        self.nod_llst = LinkedList([LLNode('come'), LLNode('go'), 'wait'])

    def test_add(self):
        self.assertEqual(self.emypty_list.add(20), True)
        self.assertEqual(self.emypty_list.add(LLNode(20)), True)
        self.one_list.add('second')
        self.assertEqual(self.one_list.get(1), 'second')

    def test_add_first(self):
        pass

    def test_add_after(self):
        pass

    def test_add_before(self):
        pass

    def test_add_at(self):
        pass

    def test_set_data(self):
        pass

    def test_remove(self):
        pass

    def test_remove_node(self):
        pass

    def test_get(self):
        with self.assertRaises(Exception):
            self.emypty_list.get(0)

        self.emypty_list.add_first(LLNode('kene'))

        with self.assertRaises(IndexError):
            self.emypty_list.get(-1)
            self.emypty_list.get(1)

        self.assertEqual(self.emypty_list.get(0), 'kene')


if __name__ == '__main__':
    unittest.main()
