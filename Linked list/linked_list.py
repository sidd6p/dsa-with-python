class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    # a linked list of three nodes:
    # 80->9->14
    def create_linked_list(self):
 
        # create and link nodes
        node1 = Node(80)
        self.head = node1
 
        node2 = Node(9)
        node1.next = node2
 
        node3 = Node(14)
        node2.next = node3
    
    def traverse_linked_list(self):
        current = self.head

        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    def append(self, data):
        new_node = Node(data)
    
        if self.head is None:
            self.head = new_node
            return
    
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_node(self, data, position = 1):
 
        # handle invalid positions
        if position < 1 or position > self.count_elements():
            print("Position Invalid")
            return
 
        new_node = Node(data)
        
        # condition to handle insertion at the beginning
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
        if self.head is None:
            return

        if position == 1:
            self.head = self.head.next
            return
    
        current = self.head
    
        if current.next is None:
            return
    
        for i in range(1, position - 1):
            if current.next is None:
                return
    
            current = current.next        
    
        current.next = current.next.next

    def reverse_linked_list(self):
        prev_node = None
        current = self.head
        next_node = current.next
    
        while True:
    
            current.next = prev_node
                    
            prev_node = current
            current = next_node
            next_node = next_node.next
                    
            if next_node == None:
                current.next = prev_node
                break
    
        self.head = current   


    def concatenate(self, list2):
        if not self.head:
            self.head = list2.head
            return
        
        current = self.head 
 
        while current.next:
            current = current.next
        
        current.next = list2.head

linked_list = LinkedList()
 
# create linked list
linked_list.create_linked_list()
