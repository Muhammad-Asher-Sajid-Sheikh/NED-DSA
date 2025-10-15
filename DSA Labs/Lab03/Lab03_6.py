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

    # Q7 — Merge two doubly linked lists
    def merge(self, other_list):
        if self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
            print("First list was empty, merged successfully.")
            return
        if other_list.head is None:
            print("Second list was empty, nothing to merge.")
            return

        # Connect tail of first list to head of second list
        self.tail.next = other_list.head
        other_list.head.prev = self.tail
        self.tail = other_list.tail

        print("Two lists merged successfully.")

# Test
dll1 = DoublyLinkedList()
dll2 = DoublyLinkedList()
for val in [1, 2, 3]:
    dll1.insertatend(val)
for val in [4, 5, 6]:
    dll2.insertatend(val)

print("List 1:")
dll1.display()
print("List 2:")
dll2.display()

dll1.merge(dll2)
print("Merged List:")
dll1.display()
