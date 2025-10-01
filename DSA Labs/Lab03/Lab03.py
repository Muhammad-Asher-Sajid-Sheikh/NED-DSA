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

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements))


    def insertatbeginning(self, new_data):
        new_node = Node(new_data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertatend(self, new_data):
            new_node = Node(new_data)

            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

    def insertafternode(self, prevnode_data, new_data):
        if self.is_empty():
            print("Cannot insert after: List is empty.")
            return

        current = self.head
        while current and current.data != prevnode_data:
            current = current.next


        if current is None:
            print(f"Cannot insert after: Node with data '{prevnode_data}' not found.")
            return

        new_node = Node(new_data)

        if current == self.tail:
            self.insertatend(new_data)
            return
        
        nextnode = current.next

        new_node.next = nextnode
        new_node.prev = current

        current.next = new_node
        nextnode.prev = new_node

    def deleteatbeginning(self):
        if self.is_empty():
            print("Cannot delete: List is empty.")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Successfully deleted the only node.")
            return

        oldhead = self.head
        
        self.head = oldhead.next
        
        self.head.prev = None
        
        oldhead.next = None
        print(f"Successfully deleted {oldhead.data} from the beginning.")

    def deleteatend(self):
        if self.is_empty():
            print("Cannot delete: List is empty.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Successfully deleted the only node.")
            return

        old_tail = self.tail
        
        self.tail = old_tail.prev
        
        self.tail.next = None
        
        old_tail.prev = None
        print(f"Successfully deleted {old_tail.data} from the end.")

    
    def deleteatposition(self, position):
        if self.is_empty():
            print("Cannot delete: List is empty.")
            return
        
        if position == 0:
            self.deleteatbeginning() 
            return

        current = self.head
        count = 0
        
        while current and count != position:
            current = current.next
            count += 1

        if current is None:
            print(f"Cannot delete: Position {position} is out of bounds.")
            return

        if current == self.tail:
            self.deleteatend()
            return

        prevnode = current.prev
        nextnode = current.next

        prevnode.next = nextnode
        
        nextnode.prev = prevnode

        current.prev = None
        current.next = None
        
        print(f"Successfully deleted node at position {position}.")

dll = DoublyLinkedList()
dll.insertatbeginning(5)
dll.insertatbeginning(6)
dll.insertatbeginning(7)
dll.insertatbeginning(8)
dll.insertatend(10)
dll.insertafternode(5, 18)
dll.deleteatposition(2)

dll.display()