from linked_list import LinkedList, LLNode


def main():
    short_list = LinkedList()
    short_list.print_list()
    short_list.print_nodes()
    # print(short_list.get(0))
    short_list.add_first(LLNode('kenex'))
    short_list.add_at(0, "kc")
    print(short_list.head.next)
    print(short_list.tail.prev)
    short_list.add("A")
    short_list.add("B")
    short_list.add("C")
    short_list.add("Kene")
    short_list.add(20)
    print(f"\nNumber of Nodes: {len(short_list)}")
    short_list.print_list()
    print(short_list.get(5))
    short_list.add_at(6, {'name': 'ken', 'type': 'IBO'})
    short_list.print_list()
    print("Removed: ", short_list.remove(6))
    short_list.print_list()
    short_list.set_data(5, {'name': 'kene', 'type': 'IBO'})
    short_list.print_list()
    short_list.print_nodes()

    node = LLNode("Testing")
    short_list.add(node)
    short_list.add("Testing1")
    short_list.print_nodes()

    short_list.add_after('B', LLNode('After B'))
    short_list.add_before('B', LLNode('Before B'))
    short_list.add_first(LLNode('First'))
    short_list.add_first('FirstElement')

    short_list.add_after("Testing", LLNode("After Testing1"))

    print()
    for node in short_list:
        print(node.print_node())
    print(f"\nNumber of Nodes: {len(short_list)}")

    dllst = LinkedList(['a', 'b', 'c'])
    dllst.print_nodes()
    dllst.print_list()
    print(f"\nNumber of Nodes: {len(dllst)}")

    dllst = LinkedList([LLNode('x'), LLNode('z'), LLNode('y')])
    dllst.print_nodes()
    dllst.print_list()
    print(f"\nNumber of Nodes: {len(dllst)}")

    dllst = LinkedList(['x', LLNode('y'), LLNode('z')])
    dllst.print_nodes()
    dllst.print_list()
    print(f"\nNumber of Nodes: {len(dllst)}")

    dllst = LinkedList(['x'])
    dllst.print_nodes()
    dllst.print_list()
    dllst.add(20)
    dllst.print_nodes()
    dllst.print_list()
    print(f"\nNumber of Nodes: {len(dllst)}")


if __name__ == "__main__":
    main()
