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
        print("Welcome, would you like to store your data in a stack, or a queue?")
        data_choice = input("Please choose:\n 's' for stack\n 'q' for queue")
        if data_choice == "s":
            data_structure = marketing_firm_creator.choose_manager_type("stack")
        elif data_choice == "q":
            data_structure = marketing_firm_creator.choose_manager_type("queue")

UI().run_simulation()
