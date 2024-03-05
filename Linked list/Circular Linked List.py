class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        """Time Complexity: O(1), Space Complexity: O(1)"""
        node1 = Node(80)
        self.head = node1
        node2 = Node(9)
        node1.next = node2
        node3 = Node(14)
        node2.next = node3
        node3.next = self.head

    def is_empty(self):
        """Time Complexity: O(1), Space Complexity: O(1)"""
        return self.head is None

    def traverse_list(self):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if self.is_empty():
            print("Empty Linked List")
            return
        current = self.head
        while current.next is not self.head:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print(f"{current.data} -> {self.head.data}")

    def append(self, data):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def node_count(self):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if self.is_empty():
            return 0
        count = 1
        current = self.head
        while current.next is not self.head:
            count += 1
            current = current.next
        return count

    def insert_at_beginning(self, data):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_position(self, data, position):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if position <= 0 or position > self.node_count() + 1:
            print("Invalid Position")
        elif position == 1:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            current = self.head
            for i in range(1, position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_from_beginning(self):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if self.is_empty():
            print("Cannot delete from Empty List")
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            del temp
        else:
            temp = self.head
            current = self.head
            while current.next is not self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head
            del temp


linked_list = CircularLinkedList()
linked_list.create_linked_list()
