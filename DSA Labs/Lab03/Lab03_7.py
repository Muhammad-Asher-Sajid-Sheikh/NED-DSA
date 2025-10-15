class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatbeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertatend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def deleteatbeginning(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print("Deleted from beginning.")

    def deleteatend(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print("Deleted from end.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")

# Q8 — Menu-driven program
dll = DoublyLinkedList()

while True:
    print("\n--- DOUBLY LINKED LIST MENU ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete at Beginning")
    print("4. Delete at End")
    print("5. Display List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        dll.insertatbeginning(val)
    elif choice == 2:
        val = int(input("Enter value: "))
        dll.insertatend(val)
    elif choice == 3:
        dll.deleteatbeginning()
    elif choice == 4:
        dll.deleteatend()
    elif choice == 5:
        dll.display()
    elif choice == 6:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
