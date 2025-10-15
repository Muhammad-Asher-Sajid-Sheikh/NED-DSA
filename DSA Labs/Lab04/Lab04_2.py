class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    
    def isEmpty(self):
        return len(self.queue) == 0

myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Dequeue: ", myQueue.dequeue())


class Queues:
    def __init__(self):
        self.queue = [None] * 5
        self.front = self.findlen()
    
    def enqueue(self, value):
        
        self.front += 1
    
    def findlen(self):
        for i in self.queue:
            self.front += 1