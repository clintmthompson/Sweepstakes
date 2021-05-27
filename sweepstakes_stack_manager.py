from stack import Stack


class SweepstakesStackManager:

    def __init__(self):
        self.name = "stack"


    def insert_sweepstakes(self, sweepstakes):
        Stack.push(sweepstakes)

    def get_sweepstakes(self):
        Stack.pop()
