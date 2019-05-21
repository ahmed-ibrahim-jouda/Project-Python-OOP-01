# Call the Father
from Recruits.recruits import Recruit

# Create a class to set he name
class Cop(Recruit):
    def __init__(self):
        super().__init__()

    # def take(self):
    #     return "i am a: cop {} \nAttack me: {} and my Attack speed: {} \nmy blood: {} and my site: {}\n********".format(self.rankarr,self.army, self.speed_atak, self.blood, self.site)

    def __str__(self):
        return "i am a: cop {} \nAttack me: {} and my Attack speed: {} \nmy blood: {} and my site: {}\n********".format(self.rankarr,self.army, self.speed_atak, self.blood, self.site)


# # test
# a1 = cop()
#
# print(a1.take())
# while a1.allalive():
#     a1.allmov()
#     print(a1.take())