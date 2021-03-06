# -*- conding: utf-8 -*-
"""Test file for linked_list data structure."""
data = ['123', '456', '789']


def test_node():
    """Test node module init method."""
    from linked_list import Node
    assert isinstance(Node(data[0]), Node)


def test_set_data():
    """Test node module set data method."""
    from linked_list import Node
    test_node = Node(data[0])
    test_node.set_data(data[1])
    assert test_node.data == data[1]


def test_set_next():
    """Test node module set next method."""
    from linked_list import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node1.set_next(test_node2)
    assert test_node1.next_node == test_node2


def test_get_data():
    """Test node module get data method."""
    from linked_list import Node
    test_node = Node(data[0])
    assert test_node.get_data() == data[0]


def test_get_next():
    """Test node module get next method."""
    from linked_list import Node
    test_node1 = Node(data[0])
    test_node2 = Node(data[1])
    test_node1.set_next(test_node2)
    assert test_node1.get_next() == test_node2


def test_linked_list():
    """Test Linked_List constructor method."""
    from linked_list import Linked_List
    assert isinstance(Linked_List(), Linked_List)


def test_insert():
    """Test Linked_List insert method."""
    from linked_list import Linked_List
    from linked_list import Node
    test_list = Linked_List()
    test_list.insert(data[0])
    assert isinstance(test_list.head, Node)


def test_pop():
    """Test Linked_List pop method."""
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(data[0])
    assert test_list.pop().data == data[0]


def test_length():
    """Test Linked_List length method."""
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(data[0])
    test_list.insert(data[1])
    assert test_list.size() == 2


def test_search():
    """Test Linked_List length method."""
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(data[0])
    test_list.insert(data[1])
    assert test_list.search(data[0]) == data[0]


def test_remove():
    """Test Linked_List remove method."""
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(data[0])
    test_list.insert(data[1])
    test_list.insert(data[2])
    test_list.remove(data[1])
    assert test_list.size() == 2


def test_display():
    """Test Linked_List display method."""
    from linked_list import Linked_List
    test_list = Linked_List()
    test_list.insert(data[0])
    test_list.insert(data[1])
    assert test_list.display() == "(123, 456)"
