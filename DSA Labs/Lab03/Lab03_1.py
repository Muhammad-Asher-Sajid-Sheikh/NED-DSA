class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insertatend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")

    def search(self, value):
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        pos = 0
        while current:
            if current.data == value:
                print(f"Value {value} found at position {pos}.")
                return
            current = current.next
            pos += 1
        print(f"Value {value} not found in the list.")

# Test
dll = DoublyLinkedList()
dll.insertatend(10)
dll.insertatend(20)
dll.insertatend(30)
dll.display()
dll.search(20)
dll.search(40)
