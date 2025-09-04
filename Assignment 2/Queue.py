class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
print("Queue peek:", queue.peek())
print("Queue dequeue:", queue.dequeue())
print("Queue size:", queue.size())
print("Queue is empty:", queue.is_empty())
