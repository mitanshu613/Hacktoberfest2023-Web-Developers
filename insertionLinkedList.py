class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:
            print("Position out of range.")
            return

        new_node.next = current.next
        current.next = new_node

# Creating a linked list and adding elements
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Displaying the original linked list
print("Original Linked List:")
my_linked_list.display()

# Inserting a node with value 4 at position 1 (0-based index)
my_linked_list.insert_at_position(4, 1)

# Displaying the modified linked list
print("Modified Linked List:")
my_linked_list.display()
