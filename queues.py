class Queues:

    def __init__(self):
        self.queues = []

    def enqueue(self, item):
        self.queues.append(item)

    def dequeue(self):
        return self.queues.pop(0)
