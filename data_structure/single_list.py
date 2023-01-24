


class SingleLinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def add(self, element):
        if not self.head:
            self.head = self.Node(element)
            return

        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def insert(self, index, element):
        if not self.head:
            print('There is no such index')
            return

        c_index = 0
        node = self.head
        prev_node = self.head

        while index > c_index:
            prev_node = node
            node = node.next_node 
            c_index += 1

        prev_node.next_node = self.Node(element, node)

    def pop(self):
        if not self.head:
            print('No data to pop')
            return

        node = self.head

        if not node.next_node:
            print(node.element)
            self.head = None
            return

        while node.next_node:
            prev_node = node
            node = node.next_node

        prev_node.next_node = None
        print(node.element)

    def print(self):
        if not self.head:
            print('No data in the list')
            return
        
        node = self.head
        print(node.element)

        while node.next_node:
            node = node.next_node
            print(node.element)


lst = SingleLinkedList()
lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.add(5)
lst.print()

print('#########')
lst.insert(2, 77)
lst.print()

print('#########')
lst.pop()
lst.pop()
lst.pop()
lst.pop()
lst.pop()
lst.pop()
lst.pop()

lst.insert(4, 444)
