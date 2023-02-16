class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0

    def add_first(self, elem):
        new_node = Node(element=elem)
        new_node.next_node = self.head
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise IndexError
        temp = self.head
        # assert isinstance(temp.next_node, object)
        self.head = temp.next_node
        temp.next_node = None
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return temp.element

    def add_last(self, elem):
        new_node = Node(element=elem)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.size += 1

    def remove_last(self):
        if self.size == 0:
            raise IndexError
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            temp = self.head
            while temp.next_node != self.tail:
                temp = temp.next_node
            self.tail = temp
            self.tail.next_node = None
            self.size -= 1


class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node
