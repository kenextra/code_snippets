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

    def test_get(self):
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.get(0)
        self.assertEqual('List is empty', str(ctx.exception))

        self.assertRaises(IndexError, self.one_list.get, -1)
        self.assertRaises(IndexError, self.one_list.get, -1)

        self.assertEqual(self.nod_llst.get(2), 'wait')

    def test_add(self):
        # adding node to emppty returns True
        self.assertEqual(self.emypty_list.add(20), True)
        self.assertEqual(self.emypty_list.add(LLNode(20)), True)

        self.one_list.add('second')
        self.assertEqual(self.one_list.get(1), 'second')

        self.two_list.add(LLNode('fourth'))
        self.assertEqual(self.two_list.get(2), 'fourth')

        # adding None, empty collection raises TypeError
        self.assertRaises(TypeError, self.one_list.add, None)
        self.assertRaises(TypeError, self.one_list.add, [])
        self.assertRaises(TypeError, self.one_list.add, {})
        self.assertRaises(TypeError, self.one_list.add, ())

    def test_add_first(self):
        # adding to empty list
        self.emypty_list.add_first('first')
        self.assertEqual(self.emypty_list.get(0), 'first')

        # add to a list with at least one node and check node is added properly
        self.one_list.add_first(LLNode('zero'))
        self.assertEqual(self.one_list.get(0), 'zero')
        self.assertEqual(self.one_list.get(1), 'first')

        # adding None, empty collection raises TypeError
        self.assertRaises(TypeError, self.one_list.add_first, None)
        self.assertRaises(TypeError, self.one_list.add_first, [])

    def test_add_after(self):
        # Linkedlist is empty
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.add_after(2, 3)
        self.assertEqual('List is empty', str(ctx.exception))

        # Linkedlist is empty
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.add_after(LLNode(2), LLNode(3))
        self.assertEqual('List is empty', str(ctx.exception))

        # Linkedlist is empty
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.add_after(LLNode(2), 3)
        self.assertEqual('List is empty', str(ctx.exception))

        # node with target_data not found
        with self.assertRaises(Exception) as ctx:
            self.one_list.add_after('second', 'third')
        self.assertEqual("Node with data second not found", str(ctx.exception))

        with self.assertRaises(Exception) as ctx:
            self.one_list.add_after(LLNode('second'), LLNode('third'))
        self.assertEqual("Node with data second not found", str(ctx.exception))

        # Add after works as expected
        self.one_list.add_after('first', 'second')
        self.assertEqual(self.one_list.get(0), 'first')
        self.assertEqual(self.one_list.get(1), 'second')

        self.two_list.add_after('second', 'before_third')
        self.assertEqual(self.two_list.get(0), 'second')
        self.assertEqual(self.two_list.get(1), 'before_third')
        self.assertEqual(self.two_list.get(2), 'third')

    def test_add_before(self):
        # Linkedlist is empty
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.add_before(2, 3)
        self.assertEqual('List is empty', str(ctx.exception))

        # Linkedlist is empty
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.add_before(LLNode(2), LLNode(3))
        self.assertEqual('List is empty', str(ctx.exception))

        # Linkedlist is empty
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.add_before(LLNode(2), 3)
        self.assertEqual('List is empty', str(ctx.exception))

        # node with target_data not found
        with self.assertRaises(Exception) as ctx:
            self.one_list.add_before('second', 'third')
        self.assertEqual("Node with data second not found", str(ctx.exception))

        with self.assertRaises(Exception) as ctx:
            self.one_list.add_before(LLNode('second'), LLNode('third'))
        self.assertEqual("Node with data second not found", str(ctx.exception))

        # Add after works as expected
        self.one_list.add_before('first', 'second')
        self.assertEqual(self.one_list.get(0), 'second')
        self.assertEqual(self.one_list.get(1), 'first')

        self.two_list.add_before('second', 'before_second')
        self.assertEqual(self.two_list.get(0), 'before_second')
        self.assertEqual(self.two_list.get(1), 'second')
        self.assertEqual(self.two_list.get(2), 'third')

    def test_add_at(self):
        # Exception when position is -ve or greater than size
        self.assertRaises(IndexError, self.emypty_list.add_at, -1, 'first')
        self.assertRaises(IndexError, self.emypty_list.add_at, 1, 'first')
        self.assertRaises(IndexError, self.two_list.add_at, 4, 'fourth')

        # Exception when data is None or empty collection
        self.assertRaises(TypeError, self.one_list.add_at, 0, None)
        self.assertRaises(TypeError, self.one_list.add_at, 0, [])

        # Adding @index zero empty list
        self.emypty_list.add_at(0, 'first')
        self.assertEqual(self.emypty_list.get(0), 'first')

        # Adding @index zero non-empty list
        self.one_list.add_at(0, 'zero')
        self.assertEqual(self.one_list.get(0), 'zero')

        # Adding @ any index
        self.nod_llst.add_at(2, 'zero')
        self.assertEqual(self.nod_llst.get(2), 'zero')
        self.assertEqual(self.nod_llst.get(3), 'wait')
        self.assertEqual(len(self.nod_llst), 4)

    def test_set_data(self):
        # Exception when position is -ve or greater than size
        self.assertRaises(IndexError, self.emypty_list.set_data, -1, 'first')
        self.assertRaises(IndexError, self.emypty_list.set_data, 0, 'first')
        self.assertRaises(IndexError, self.two_list.set_data, 2, 'first')

        # Exception when data is None or empty collection
        self.assertRaises(TypeError, self.one_list.set_data, 0, None)
        self.assertRaises(TypeError, self.two_list.set_data, 0, [])

        # changing data at an index
        data = self.one_list.set_data(0, 'second')
        self.assertEqual(data, 'first')
        self.assertEqual(self.one_list.get(0), 'second')
        self.assertEqual(len(self.one_list), 1)

        data = self.nod_llst.set_data(1, 'here')
        self.assertEqual(data, 'go')
        self.assertEqual(self.nod_llst.get(1), 'here')
        self.assertEqual(len(self.nod_llst), 3)

    def test_remove_at(self):
        # Exception when position is -ve or greater than size
        self.assertRaises(IndexError, self.emypty_list.remove_at, -1)
        self.assertRaises(IndexError, self.emypty_list.remove_at, 0)
        self.assertRaises(IndexError, self.two_list.remove_at, 2)

        # removing data at an index
        data = self.one_list.remove_at(0)
        self.assertEqual(data, 'first')
        self.assertEqual(len(self.one_list), 0)

        data = self.nod_llst.remove_at(1)
        self.assertEqual(data, 'go')
        self.assertEqual(self.nod_llst.get(1), 'wait')
        self.assertEqual(len(self.nod_llst), 2)

    def test_remove_node(self):
        # Exception when position try to remove from empty list
        with self.assertRaises(Exception) as ctx:
            self.emypty_list.remove_node('x')
        self.assertEqual("List is empty", str(ctx.exception))

        # Exception when node does not exist
        with self.assertRaises(Exception) as ctx:
            self.nod_llst.remove_node('here')
        self.assertEqual("Node with data here not found", str(ctx.exception))

        # removing node at any position
        self.one_list.remove_node('first')
        self.assertEqual(len(self.one_list), 0)

        self.nod_llst.remove_node('go')
        self.assertEqual(self.nod_llst.get(1), 'wait')
        self.assertEqual(self.nod_llst.get(0), 'come')
        self.assertEqual(len(self.nod_llst), 2)


if __name__ == '__main__':
    unittest.main()
