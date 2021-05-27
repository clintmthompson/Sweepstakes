import marketing_firm_creator
import sweepstakes
from sweepstakes import Sweepstakes
from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager


class Manager:

    def __init__(self, manager):
        self.manager = manager


    def create_sweepstakes(self, name):
        return sweepstakes.Sweepstakes(name)

#   def store_sweepstakes(self, sweepstakes):
#       if self.manager.
