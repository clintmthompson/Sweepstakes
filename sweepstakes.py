from contestants import Contestant
import random


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
        new_contestant = contestant
        self.contestants_list.append({f"'first_name': {new_contestant.first_name}, 'last_name': {new_contestant.last_name}, 'email': {new_contestant.email}, 'registration_number': {new_contestant.registration_number}"})

    def pick_winner(self):
        winner = self.contestants_list[random.randint(0, len(self.contestants_list)-1)]
        self.print_contestant_info(winner)
        return winner

    def print_contestant_info(self, contestant):
        print(f"Congratulations to our winner, {contestant['first_name']} {contestant['last_name']}!!!")
