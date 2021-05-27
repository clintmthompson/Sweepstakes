import marketing_firm
import queues
import sweepstakes_queue_manager
import sweepstakes_stack_manager


def choose_manager_type(type):
    if type == "queue":
        manager = marketing_firm.Manager("queue")
        return manager
    elif type == "stack":
        manager = marketing_firm.Manager("stack")
        return manager
