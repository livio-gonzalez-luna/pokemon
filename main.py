from fight import Fight
from pokedex import Pokedex


class PokemonGame:
    def __init__(self):
        self.running = True
    
    def run(self):
        menu = (
            "\n------------------------\n"
            "What would you like to do?\n"
            "1. Play\n"
            "2. Go to Pokedex\n"
            "3. Quit"
        )
        
        while self.running:
            print(menu)
            choice = input("Enter your choice: ")
            
            if choice == "1":
                fight = Fight()
                fight.fight()
                
            elif choice == "2":
                pokedex = Pokedex()
                pokedex.run()
                
            elif choice == "3":
                self.running = False
                
            else:
                print("Invalid choice, try again...")


# Run PokemonGame
game = PokemonGame()
game.run()
