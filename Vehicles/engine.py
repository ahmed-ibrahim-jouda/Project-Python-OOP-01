# Call library generate random numbers
from random import randint
# Create a class to generate a site and live for the platoon
class Engine:
    # LIST that contains weapons and give it randomly to the personality

    amo = ["The rockets", "Missiles", "Cartridges", "Nuclear missile", "Atomic missile", "Hydrogen rocket", "Spray", "Sound waves"]
    # Site generation and life
    def __init__(self, Vehicle_condition=100, full=100, spot=(0, 0)):
        self.full = full
        self.Vehicle_condition = Vehicle_condition
        self.spot = spot
        self.speed_atak = randint(500, 50000)
        self.amos = self.amo[randint(0, len(self.amo) - 1)]
    # Move the personal
    def allmov(self):

        if self.Vehicle_condition>0:
            self.Vehicle_condition -= randint(0, self.Vehicle_condition)
            self.full -= randint(0, self.full)

            if self.full > 0:
                self.spot = (randint(-100, 100), randint(-100, 100))

    # Examine life personal
    def allalive(self):

        if self.Vehicle_condition > 0:
            return True
        else:
            return False

            # Is the character dead

    def endgamme(self):
        if self.Vehicle_condition == 0:
            return True
        else:
            return False