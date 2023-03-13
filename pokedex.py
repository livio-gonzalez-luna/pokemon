import json

with open('pokedex.json', 'r') as f:
    pokemonData = json.load(f)

with open('pokemonDescription.json', 'r') as f:
    pokemonDescription = json.load(f)



class Pokedex:
    def __init__(self):
        self.pokemonData = pokemonData


    def showList(self):
        print("\nHere are all the available Pokemon in the Pokedex:")
        print("-" * 40)
        for pokemon in self.pokemonData:
            print(pokemon)
        print("-" * 40)

    def show_pokemon_info(self, name):
        pokemonId = self.pokemonData[name]['pokedexId']
        pokemonType = self.pokemonData[name]['type']
        pokemonSpecy = self.pokemonData[name]['species']
        pokemonHeight = self.pokemonData[name]['height']
        pokemonWeight = self.pokemonData[name]['weight']
        pokemonDescriptionPerso = pokemonDescription[name]
        pokemonhp = self.pokemonData[name]["baseStats"]['hp']
        for pokemon in self.pokemonData:
            if name == pokemon:
                print(f"\n{pokemon} Info:")
                print("-" * 40)
                print(f"ID: {pokemonId}")
                print(f"Type: {pokemonType}")
                print(f"Species: {pokemonSpecy}")
                print(f"Height: {pokemonHeight}")
                print(f"Weight: {pokemonWeight}")
                print("-" * 40)
                print(f"{pokemon} Description:\n{pokemonDescriptionPerso}")
                print("-" * 40)
                print("Base Stats:")
                print(f"Health: {pokemonhp}")
        else:
            print("Pokemon not found!")

    def run(self):
        self.running = True
        Pokedex.showList(self)
        while self.running:
            pokemonchoosen = input("Enter a pokemon name: ")
            Pokedex.show_pokemon_info(self, pokemonchoosen)
            choice = input("Do you want to see another pokemon? (y/n): ")
            if choice == "y":
                Pokedex.showList(self)
            elif choice == "n":
                self.running = False
            else:
                print("Invalid choice, try again...")
   
# Example usage
pokedex = Pokedex()
pokedex.run()



