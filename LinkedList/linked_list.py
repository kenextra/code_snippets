class LLNode:
    """A class that defines a linked list node

    Attributes
    ----------
    data : Any
        Data element for the node
    prev : LLNode
        Previous node this node points to (default=None)
    next : LLNode
        next node this node points to (default=None)
    """

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.data})")

    def print_node(self):
        """Prints the node in a pretty format
        """
        return (f"{self.__class__.__name__}({self.data}) --> "
                f"[data: {self.data}, "
                f"prev: {self.prev if self.prev.data else 'Head'}, "
                f"next: {self.next if self.next.data else 'Tail'}]")


class LinkedList:
    """A class that implements a doubly linked list

    Attributes
    -------
    size : int
        number of elements in the linked list
    head : LLNode
        head of the linked list
    tail : LLNode
        tail of the linked list
    """

    def __init__(self, nodes=None):
        self.head = LLNode()
        self.tail = LLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        if nodes is None:
            self.size = 0
        else:
            self.size = 1
            data = nodes.pop(0)
            node = data if isinstance(data, LLNode) else LLNode(data=data)
            self.head.next = node
            for elem in nodes:
                is_llnode = isinstance(elem, LLNode)
                node.next = elem if is_llnode else LLNode(data=elem)
                node.prev = self.tail.prev
                self.tail.prev = node
                node = node.next
                self.size += 1
            self.tail.prev = node
            node.next = self.tail

    def __iter__(self):
        """Yields the next node in a linked list

        Yields
        -------
        LLNode
            The next node in the linked list
        """
        node = self.head.next
        while node.data is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def print_list(self):
        """Prints the linkedlist in a pretty format
        """
        print(f"\nHead[{self.head}]", end='')
        node = self.head.next
        while node.data is not None:
            print(" ->", node, end='')
            node = node.next
        print(f" -> Tail[{node}]")

    def print_nodes(self):
        """Prints the linkedlist in a pretty format without head and tail
        """
        if self.size == 0:
            print("Add nodes to the linked list")
            return

        print()
        node = self.head.next
        while node.data is not None:
            if node.next == self.tail:
                print(node)
            else:
                print(node, "-> ", end='')
            node = node.next

    def add_first(self, node):
        """Add a node or element to the first index

        Parameters
        ----------
        node : [Any, LLNode]
            Node or element to be added
        """
        first_node = self.head.next
        if not first_node.next:  # if it is linkedlist tail
            self.add(node)
            return
        if not isinstance(node, LLNode):
            node = LLNode(node)
        node.next = first_node
        node.prev = self.head
        self.head.next = node
        first_node.prev = node
        self.size += 1

    def add(self, data):
        """Appends data or node to the end of the list

        Parameters
        ----------
        data : Any, LLNode
            The data or node to add

        Returns
        -------
        bool
            True if the element was added succesfully

        Raises
        ------
        TypeError
            if element is NoneType
        """
        if data is None:
            raise TypeError
        if isinstance(data, LLNode):
            node = data
        else:
            node = LLNode(data)
        node.prev = self.tail.prev
        node.next = node.prev.next
        node.next.prev = node
        node.prev.next = node
        self.size += 1

        return True

    def add_after(self, target_node_data, new_node):
        """Add a new node after the given target node data

        Parameters
        ----------
        target_node_data : Any
            Data element of the target Node
        new_node : LLNode
            The new node to be added

        Raises
        ------
        Exception
            if list is empty or node with data not found
        """
        node = self.head.next
        if not node.next:  # if it is linkedlist tail
            raise Exception("List is empty")

        tail_prev = self.tail.prev
        if tail_prev.data == target_node_data:
            return self.add(new_node)

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                new_node.prev = node
                node.next.prev = new_node
                node.next = new_node
                self.size += 1
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data, new_node):
        """Add a new node before the given target node data

        Parameters
        ----------
        target_node_data : Any
            Data of the target node
        new_node : LLNode
            The new node or element to be added

        Raises
        ------
        Exception
            if list is empty or node with data not found
        """
        first_node = self.head.next
        if not first_node.next:  # if it is linkedlist tail
            raise Exception("List is empty")

        if first_node.data == target_node_data:
            self.add_first(new_node)
            return

        prev_node = self.head.next  # first_node
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                new_node.prev = prev_node
                node.prev = new_node
                self.size += 1
                return
            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")

    def get(self, index):
        """Get the data at position index

        Parameters
        ----------
        index : int
            position index

        Returns
        -------
        Any
            Data in the node of position index

        Raises
        ------
        Exception
            if the list is empty
        IndexError
            if the index is out of bounds
        """
        node = self.head.next
        if not node.next:  # if it is linkedlist tail
            raise Exception("List is empty")

        if index < 0 or index > self.size:
            raise IndexError

        count = 0
        while node != self.tail:
            if count == index:
                data = node.data
                return data
            count += 1
            node = node.next

    def add_at(self, index, data):
        """Add node with data to the list at the specified index

        Parameters
        ----------
        index : int
            The index where the data node should be added
        data : Any
            The data to add

        Raises
        ------
        IndexError
            if the index is out of bounds
        """
        if (index < 0 or index > self.size) and (index != 0 or self.size != 0):
            raise IndexError
        if index == 0:
            self.add_first(data)
            return
        self.add(data)
        node = self.tail.prev
        count = self.size - 1

        while count != index:
            node.data = node.prev.data
            node = node.prev
            count -= 1
        node.data = data

    def remove(self, index):
        """Remove a node at the specified index and return its data elemet

        Parameters
        ----------
        index : int
            The index of the node to remove

        Returns
        -------
        Any
            The data removed

        Raises
        ------
        IndexError
            if index is out of bounds of list
        """
        node = self.head.next
        count = 0

        if index < 0 or index >= self.size:
            raise IndexError
        while node != self.tail:
            if count == index:
                data = node.data
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
            count += 1
            node = node.next
        return data

    def set_data(self, index, data):
        """Set an index position in the list to a new data

        Parameters
        ----------
        index : int
            The index of the node to change its data
        data : Any
            The new data

        Returns
        -------
        Any
            The data that was replaced

        Raises
        ------
        IndexError
            if the index is out of bounds
        """
        node = self.head.next
        count = 0

        if index < 0 or index >= self.size:
            raise IndexError

        while node != self.tail:
            if count == index:
                prev_data = node.data
                node.data = data
                return prev_data
            count += 1
            node = node.next
        return None
