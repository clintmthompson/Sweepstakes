from queues import Queue


class SweepstakesQueueManager:

    def __init__(self):
        pass

    def insert_sweepstakes(self, sweepstakes):
        Queue.enqueue(sweepstakes)

    def get_sweepstakes(self):
        Queue.dequeue()
