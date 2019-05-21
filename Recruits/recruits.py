# Call library generate random numbers
from random import randint
# Create a class to generate a site and live for the platoon
class Recruit:
    # A group of lysets that contain graded weapons and give them a random character
    rankar = ["general","major general","colonel","major","Army","Seaman","Flying Pilot","Lieutenant colonel"]
    arm = ["gun", "Kalashnikov", "RBJ", "M4", "M66", "Sword", "Plane", "tanker"]
    # Site generation and life
    def __init__(self, blood=100, site=(0, 0)):
        self.blood = blood
        self.site = site
        self.speed_atak = randint(500, 10200)
        self.rankarr = self.rankar[randint(0, len(self.rankar)-1)]
        self.army = self.arm[randint(0, len(self.arm) - 1)]
    # Move the personal
    def allmov(self):
        if self.blood > 0:
            self.site = (randint(-100, 100), randint(-100, 100))
            self.blood -= randint(0, self.blood)
    # Examine life personal
    def allalive(self):
        if self.blood > 0:
            return True
        else:
            return False

        # Is the character dead
    def endgamme(self):
        if self.blood == 0:
            return True
        else:
            return False