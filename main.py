import contestants
import marketing_firm
import sweepstakes
from marketing_firm import Manager
import marketing_firm_creator


jimmy_pesto = marketing_firm.Manager("Jimmy Pesto")
sweeps = jimmy_pesto.create_sweepstakes()
sweeps.register_contestant(contestants.Contestant("Sally", "Fields", "sally@aol.com", 4))
sweeps.pick_winner()
