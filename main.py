import contestants
import marketing_firm
import sweepstakes
from marketing_firm import Manager
import marketing_firm_creator

sweeps = sweepstakes.Sweepstakes("Sweeps")
print(sweeps.contestants_list)

sweeps.register_contestant(contestants.Contestant("Matt", "Bollocks", "email", 4))

print(sweeps.contestants_list)
sweeps.pick_winner()
