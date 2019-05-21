# Call library generate random numbers
from random import randint

# Create a class to generate a site and live for the platoon
class AnimalContent:
    # Site generation and life
    def __init__(self, life=100, loc=(0, 0)):
        self.life = life
        self.loc = loc
        self.speed_atak = randint(100, 10002)

    # Move the personal
    def allmov(self):
        if self.life > 0:
            self.loc = (randint(-100, 100), randint(-100, 100))
            self.life -= randint(0, self.life)

    # Examine life personal
    def allalive(self):
        if self.life > 0:
            return True
        else:
            return False

    # Is the character dead
    def endgamme(self):
        if self.life == 0:
            return True
        else:
            return False
