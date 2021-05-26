from contestants import Contestant


class Sweepstakes:

    def __init__(self, name):
        self.name = name

        self.contestants_list = [
            {
                "first_name": "Bill",
                "last_name": "Dauterive",
                "email": "bill4387@gmail.com",
                "registration_number": 1
            },
            {
                "first_name": "Hank",
                "last_name": "Hill",
                "email": "propane_god@strickland.com",
                "registration_number": 2
            },
            {
                "first_name": "Rusty",
                "last_name": "Shackleford",
                "email": "dales_dead_bug@hotmail.com",
                "registration_number": 3
            },
        ]

    def register_contestant(self, contestant):
        pass

    def pick_winner(self):
        pass

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
