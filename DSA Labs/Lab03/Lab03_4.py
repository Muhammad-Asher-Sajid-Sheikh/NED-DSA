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

    def deleteatposition(self, position):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        count = 0

        if position == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            print("Deleted node at position 0.")
            return

        while current and count < position:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        # If deleting the last node
        if current.next is None:
            current.prev.next = None
            self.tail = current.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        print(f"Deleted node at position {position} with value {current.data}.")

# Test
dll = DoublyLinkedList()
dll.insertatend(10)
dll.insertatend(20)
dll.insertatend(30)
dll.insertatend(40)
dll.display()
dll.deleteatposition(3)  # delete last node without deleteAtEnd()
dll.display()
