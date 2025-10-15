class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatend(self, data):
        new_node = Node(data)
        if self.head is None:
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

    # Q3 — Count total nodes
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Total nodes in list: {count}")

# Test
dll = DoublyLinkedList()
dll.insertatend(5)
dll.insertatend(15)
dll.insertatend(25)
dll.display()
dll.count_nodes()
