# Call the Father
from Vehicles.engine import Engine

# Create a class to set he name
class Tank(Engine):
    def __init__(self):
        super().__init__()

    def take(self):
        return "i am a: tank\nAttack by: {} and my Attack speed: {}\nmy full: {} my Vehicle: {} and my site: {}\n********".format(self.amos, self.speed_atak, self.full, self.Vehicle_condition, self.spot)

    def __str__(self):
        return "i am a: tank\nAttack by: {} and my Attack speed: {}\nmy full: {} my Vehicle: {} and my site: {}\n********".format(self.amos, self.speed_atak, self.full, self.Vehicle_condition, self.spot)

# # test
# a1 = tank()
#
# print(a1.take())
# while a1.allalive():
#     a1.allmov()
#     print(a1.take())