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

    def traverse(self):
        """
        Time: O(n)
        Space(1)
        """
        current = self.head

        while current is not None:
            print(f"{current.data} <-> ", end="")
            current = current.next
        print("None")

    def reverse_traverse(self):
        """
        Time: O(n)
        Space: (1)
        """
        current = self.tail

        print("None", end = " <-> ")
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.prev
        print("None")


    def node_count(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, data):
        """
        Time: O(1)
        Space: O(1)
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_beginning(self, data):
        """
        Time: O(1)
        Space: O(1)
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_at_position(self, data, position):
        """
        Time: O(n)
        Space: O(1)
        """
        if position <= 0  or position > self.node_count():
            print("Invalid position")
            return          
        elif position == 1:
            self.insert_at_beginning(data)
            return
        elif position == self.node_count():
            self.append(data)
            return 
        else:
            new_node = Node(data)
            current = self.head

            for idx in range(1, position - 1):
                current = current.next
            next_node = current.next
            current.next = new_node
            next_node.prev = new_node
            new_node.prev = current
            new_node.next = next_node

            return
        
    def delete_from_beginning(self):
        """
        Time: O(1)
        Space: O(1)
        """
        if self.node_count() == 0:
            print('Cannot delete from Empty')
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else: 
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            del current

    def delete_from_end(self):
        """
        Time: O(1)
        Space: O(1)
        """
        if self.node_count() == 0:
            print('Cannot delete from Empty')
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else:
            cur = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del cur            

    def delete_from_position(self, position):
        """"
        Time: O(n)
        Space: O(1)
        """
        if self.node_count() == 0:
            print('Cannot delete from Empty')
        elif position <= 0 or position > self.node_count():
            print("Invalid position")
        elif position == 1:
            self.delete_from_beginning()
        elif position == self.node_count():
            self.delete_from_end()
        else:
            current = self.head
            prev_node = next_node = None
            for idx in range(position - 1):
                current = current.next
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next.node.prev = prev_node

            del current

    def reverse(self):
        if self.node_count() < 2:
            return
        else:
            current = self.head

            while True:
                current.prev, current.next = current.next, current.prev
                current = current.prev

                if current == None:
                    break
            self.head, self.tail = self.tail, self.head
            return
        
linked_list = DoublyLinkedList()
linked_list.create_linked_list()