"""
TODO:
    - tail
    - метод delete
    - метод clear
    - __iter__
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional



@dataclass
class SingleLinkedList:
    head: Optional[Node] = None
    length: int = 0

    @dataclass
    class Node:
        element: Any = None
        next_node: Optional[SingleLinkedList.Node] = None

    def append(self, element):
        self.length += 1
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
        
        self.length += 1

        c_index = 0
        node = self.head
        prev_node = self.head

        if index == 0:
            node = self.head
            self.head = self.Node(element, node)
            return

        while index > c_index:
            prev_node = node
            node = node.next_node 
            c_index += 1

        prev_node.next_node = self.Node(element, node)

    def pop(self):
        if not self.head:
            print('No data to pop')
            return

        self.length -= 1

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
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
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
