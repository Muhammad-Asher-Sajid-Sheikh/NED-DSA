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

    # Q6 — Reverse the doubly linked list
    def reverse(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        temp = None

        # Swap prev and next for all nodes
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev  # move to next (which is prev before swap)

        # Adjust head and tail
        if temp:
            self.head = temp.prev

        print("List reversed successfully.")

# Test
dll = DoublyLinkedList()
dll.insertatend(10)
dll.insertatend(20)
dll.insertatend(30)
dll.insertatend(40)
dll.display()
dll.reverse()
dll.display()
