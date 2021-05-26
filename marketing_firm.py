import sweepstakes
from sweepstakes import Sweepstakes


class Manager:

    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstakes_list = [sweepstakes.Sweepstakes("Mega Millions").contestants_list]
        return sweepstakes_list
