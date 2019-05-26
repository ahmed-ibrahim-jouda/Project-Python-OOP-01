# import Folder containing all characters
from Character.import_all import *
# import The folder that contains the game runs
from Character.cartier import Cartier

# Definition of characters
figures1 = [Falcon(), Armored_corps(), Cop()]
figures2 = [Cat(), Armored_corps(), Cop()]

# Defining the first player
player1 = Cartier("Amir", figures1)

# Second player definition
player2 = Cartier("Ahmed", figures2)

while True:

    print("_____Confrontation_____")
    player1.playing()
    print("ـــــــــــــــــــــــ")
    player2.playing()
    print("_____End Confrontation_____\n")
    if player1.stop_loop() :
        print("THE Weener IS",player2.Cartier_name)
        break
    elif player2.stop_loop() :
        print("THE Weener IS",player1.Cartier_name)
        break

