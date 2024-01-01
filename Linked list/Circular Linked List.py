class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

        node3.next = self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def traverse_list(self):
        if self.is_empty():
            print('Empty Linked List')
            return
        
        current = self.head
        while current.next is not self.head:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print(f"{current.data} -> {self.head.data}")

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def node_count(self):
        if self.is_empty():
            return 0
        count = 1
        current = self.head
        while current.next is not self.head:
            count += 1
            current = current.next
        return count
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
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
        if position <= 0 or position > self.node_count() + 1:
            print("Invalid Position")
        elif position == 1:
            self.insert_at_beginning(data)
        elif position == self.node_count() + 1:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            
            for i in range(1, position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node

    # delete from beginning
    def delete_from_beginning(self):
        # check if the linked list is empty
        if self.is_empty():
            print('Cannot delete from Empty List')
        # check if the circular linked list has only one node
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            del temp
        else:
            # get a reference to head
            temp = self.head
            current = self.head
            # get a reference to the last node
            while current.next is not self.head:
                current = current.next
            # shift head to second node    
            self.head = self.head.next
            # adjust the next pointer of the last node to the new head
            current.next = self.head
            del temp
            
linked_list = CircularLinkedList()
linked_list.create_linked_list()