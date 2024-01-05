class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_linked_list(self):
        node1 = Node(10)
        self.head = node1
        self.tail = node1

        node2 = Node(100)
        node1.next = node2
        node2.prev = node1

        node3 = Node(1000)
        node2.next = node3
        node3.prev = node2

        self.tail = node3

linked_list = DoublyLinkedList()
linked_list.create_linked_list()