import marketing_firm
import sweepstakes_queue_manager
import sweepstakes_stack_manager


def choose_manager_type(type):
    if type == "queue":
        data_structure = sweepstakes_queue_manager.SweepstakesQueueManager()
        return data_structure
    elif type == "stack":
        data_structure = sweepstakes_stack_manager.SweepstakesStackManager()
        return data_structure
