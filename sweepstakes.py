from contestants import Contestant


class Sweepstakes:

    def __init__(self, name):
        self.name = name

    def register_contestant(self, contestant):
        pass

    def pick_winner(self):
        pass

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
