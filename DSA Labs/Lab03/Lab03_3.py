class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")

    def insertatposition(self, position, data):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        # If inserting at the end (last position)
        if current.next is None:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        else:
            new_node.next = current.next
            current.next.prev = new_node
            new_node.prev = current
            current.next = new_node

# Test
dll = DoublyLinkedList()
dll.insertatposition(0, 10)
dll.insertatposition(1, 20)
dll.insertatposition(2, 30)
dll.insertatposition(3, 40)  # inserting at last without insertAtEnd()
dll.display()
