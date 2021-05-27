import contestants
import marketing_firm
import sweepstakes
from marketing_firm import Manager
import marketing_firm_creator



class UI:

    def __init__(self):
        pass

    def run_simulation(self):
        self.choose_manager_prompt()

    def choose_manager_prompt(self):
        print("\nWelcome, would you like to store your data in a stack, or a queue?\n")
        data_choice = input("Please choose:\n 's' for stack\n 'q' for queue\n")
        if data_choice == "s":
            my_manager = Manager(marketing_firm_creator.choose_manager_type("stack"))
        elif data_choice == "q":
            my_manager = Manager(marketing_firm_creator.choose_manager_type("queue"))
        my_manager
        self.options_menu(my_manager)

    def options_menu(self, manager):
        print("Please choose from the following options")
        options = input("1 - Create a new sweepstakes\n2 - Add new contestant\n")

        if options == "1":
            sweep_name = input("What would you like to call the Sweepstakes\n?")
            new_sweeps = manager.create_sweepstakes(sweep_name)
            print(new_sweeps.contestants_list)
            print(f"You generated a new sweepstakes called {new_sweeps.name}")
        if options == "2":
            first_name = input("Enter first name")
            last_name = input("Enter first name")
            email = input("Enter email")
            id = input("Enter registration number")
            contestant = contestants.Contestant(first_name, last_name, email, id)
            sweepstakes.Sweepstakes(contestant)
            print(f'Contestant {contestant.first_name} has been added')

        self.options_menu(manager)


UI().run_simulation()
