import sweepstakes
from sweepstakes import Sweepstakes
from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager


class Manager:

    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        return sweepstakes.Sweepstakes("Mega Millions")
