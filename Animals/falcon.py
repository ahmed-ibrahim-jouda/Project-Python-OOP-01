# Call the Father
from Animals.anim import AnimalContent

# Create a class to set he name
class Falcon(AnimalContent):
    def __init__(self, attack="teeth"):
        super().__init__()
        self.animal_attack = attack

    # def take(self):
    #     return "i am a: falcon animals \nMy offensive abilities: {} and my Attack speed: {} \nmy life: {} and my locashen: {}\n********".format(self.animal_attack, self.speed_atak, self.life, self.loc)

    def __str__(self):
        return "i am a: falcon animals \nMy offensive abilities: {} and my Attack speed: {} \nmy life: {} and my locashen: {}\n********".format(
            self.animal_attack, self.speed_atak, self.life, self.loc)

# # test
# a1 = Falcon()
# while True:
#
#     a1.allmov()
#     print(a1)
#     if a1.endgamme():
#         break

