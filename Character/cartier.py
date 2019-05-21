# Define class players
class Cartier:
    # Bring items to aray and pleyer  name
    def __init__(self, name="", cart=list()):
        self.cart = cart
        self.Cartier_name = name
        self.di = 0

    def stop_loop(self):

        return all([n.endgamme() for n in self.cart])


    # Prints background information for playing time
    def playing(self):

        print("Role", self.Cartier_name)

        for n in self.cart:

            if n.allalive():
                print(n)
                n.allmov()
