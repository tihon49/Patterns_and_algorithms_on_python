class DoubleLinkedList:
    head = None
    tail = None
    len = 0

    class Node:
        def __init__(self, element, prev_node=None, next_node=None):
            self.element = element
            self.prev_node = prev_node
            self.next_node = next_node

    def append(self, element):
        """Вставка в конец списка за O(1)
        Так как не нужно проходиться по всему списку,
        а сразу переходим к tail элементу.

        Args:
            element (Any): Some element
        """
        if not self.head:
            new_node = self.Node(element)
            self.head = new_node
            self.tail = new_node
            self.len += 1
            return

        node = self.tail
        new_node = self.Node(element, prev_node=node)
        node.next_node = new_node
        self.tail = new_node
        self.len += 1

    def pop(self):
        if not self.tail:
            print("Cant pop from empty list")
            return

        tail = self.tail
        if tail == self.head:
            print(tail.element)
            self.head = None
            self.tail = None
            self.len = 0
            return

        pre_tail_node = tail.prev_node
        print(tail.element)
        tail = None
        pre_tail_node.next_node = None
        self.tail = pre_tail_node
        self.len -= 1

    def insert(self, index, element):
        if not self.head:
            print("There is no such index")
            return

        self.len += 1

        c_index = 0
        node = self.head
        prev_node = self.head

        while index > c_index:
            prev_node = node
            node = node.next_node
            c_index += 1

        new_node = self.Node(
            element,
            prev_node=prev_node,
            next_node=prev_node.next_node,
        )
        prev_node.next_node.prev_node = new_node
        prev_node.next_node = new_node

    def print(self):
        if not self.head:
            print("List is empty")
            return

        node = self.head
        print(node.element)
        while node.next_node:
            node = node.next_node
            print(node.element)


l = DoubleLinkedList()
l.append(1)
l.append(2)

l.print()
