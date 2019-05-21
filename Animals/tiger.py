# Call the Father
from Animals.anim import AnimalContent


# Create a class to set he name
class Tiger(AnimalContent):
    def __init__(self, attack="Speed Attack"):
        super().__init__()
        self.animal_attack = attack

    # def take(self):
    #     return "i am a: tiger animals \nMy offensive abilities: {} and my Attack speed: {} \nmy life: {} and my locashen: {}\n********".format(self.animal_attack, self.speed_atak, self.life, self.loc)

    def __str__(self):
        return "i am a: tiger animals \nMy offensive abilities: {} and my Attack speed: {} \nmy life: {} and my locashen: {}\n********".format(
            self.animal_attack, self.speed_atak, self.life, self.loc)

# # test
# a1 = cat()
# while True:
#     print(a1)
#     a1.allmov()
#     if a1.endgamme():
#         break
