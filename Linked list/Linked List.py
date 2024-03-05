class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def traverse_linked_list(self):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    def append(self, data):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_node_at_beginning(self, data):
        """Time Complexity: O(1), Space Complexity: O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def count_elements(self):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if self.head is None:
            return 0
        count = 1
        current = self.head
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def insert_node_at_position(self, data, position=1):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        # handle invalid positions
        if position < 1 or position > self.count_elements() + 1:
            print("Position Invalid")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(1, position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, position):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if self.head is None:
            return
        if position == 1:
            self.head = self.head.next
            return
        current = self.head
        for i in range(1, position - 1):
            if current.next is None:
                return
            current = current.next
        temp = current.next
        current.next = current.next.next
        del temp

    def reverse_linked_list(self):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        prev_node = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def concatenate(self, list2):
        """Time Complexity: O(n), Space Complexity: O(1)"""
        if self.head is None:
            self.head = list2.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = list2.head
