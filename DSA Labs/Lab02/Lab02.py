# LAB SESSION 02 - Singly Linked List Operations in Python

# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class with required operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Traverse and print list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # 1. Insert at the beginning
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 2. Delete the last node
    def deleteLast(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # 3. Count total nodes
    def countNodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # 4. Search for a value
    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return f"Value {key} found at position {pos}"
            temp = temp.next
            pos += 1
        return f"Value {key} not found"

    # 5. Reverse the list iteratively
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    # 6. Sort the linked list (ascending)
    def sortList(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    ll = LinkedList()

    # Create initial list: 10 -> 20 -> 30
    ll.insertAtEnd(10)
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    print("Initial Linked List:")
    ll.printList()

    # Insert at beginning
    ll.insertAtBeginning(5)
    print("\nAfter inserting 5 at beginning:")
    ll.printList()

    # Delete last node
    ll.deleteLast()
    print("\nAfter deleting last node:")
    ll.printList()

    # Count nodes
    print("\nTotal nodes:", ll.countNodes())

    # Search value
    print(ll.search(20))
    print(ll.search(100))

    # Reverse list
    ll.reverse()
    print("\nAfter reversing:")
    ll.printList()

    # Insert unsorted values and then sort
    ll.insertAtEnd(15)
    ll.insertAtEnd(2)
    ll.insertAtEnd(50)
    print("\nBefore sorting:")
    ll.printList()

    ll.sortList()
    print("\nAfter sorting:")
    ll.printList()
