
import json
import random
from pokemon import Pokemon

with open('pokemonList.json') as pokemonList:
    pokemonData = json.load(pokemonList)

with open('pokemonMove.json') as attackTypes:
    attackMove = json.load(attackTypes)

with open('pokedex.json') as pokedex:
    pokedexFile = json.load(pokedex)

class Fight:
    def __init__(self):
        self.playerPokemon = None
        self.opponentPokemon = None
        self.player = None
        self.opponent = None

    def bag(self):
        print("\nYou have no items in your bag.")

    def pokemon(self):
        print("\nYou have no other pokemon.")

    def run(self):
        print("\nYou can't run from a trainer battle!")

    def playerPokemonChoice(self):
        validPokemon = []
        for name in pokedexFile:
            validPokemon.append(name)
        print(f"Your pokedex: {validPokemon}")
        choosenPokemon = input(f"Choose your pokemon from your pokedex: ")
        while choosenPokemon not in validPokemon:
            print("Invalid pokemon choice!")
            choosenPokemon = input(f"Choose your pokemon from your pokedex: {validPokemon}\n")
        self.playerPokemon = Pokemon(choosenPokemon)

 
    def playerTurn(self):  
        print("\nWhat will " + self.playerPokemon._name + " do?")
        print("1. Attack")
        print("2. Bag")
        print("3. Pokemon")
        print("4. Run")
        choice = input("Enter a number: ")
        if choice == "1":
            movesName = []
            for move in self.playerPokemon.move:
                movesName.append(move)
            print(f"\nWhat move will {self.playerPokemon._name} use?")
            for move in movesName:
                print(move)
            move = input('Enter a move: ')
            while move not in movesName:
                print('Invalid move!')
                move = input('Enter a move: ')
            moveName = self.playerPokemon.move[movesName.index(move)]
            damage = self.playerPokemon.performAttack(self.opponent, moveName)   
            print()   
            print(self.playerPokemon._name + f" dealt {round(damage, 2)} damage to {self.opponent._name}!")
            print(f"{self.opponent._name} has {round(self.opponent._hp, 2)} HP left!")
        elif choice == "2":
            self.bag()
        elif choice == "3":
            self.pokemon()
        elif choice == "4":
            self.run()


    def opponentPokemonChoice(self):
        validPokemon = [pokemonData["name"] for pokemonData in pokemonData.values()]
        self.opponentPokemon = Pokemon(random.choice(validPokemon))

    def opponentTurn(self):
        randomOpponentAttack = random.choice(self.opponent.move)

        if self.opponent._hp > 0:
            print(self.opponent._name + " used " + randomOpponentAttack + "!")
            damage = self.opponent.performAttack(self.player, randomOpponentAttack)
            print(self.opponent._name + f" dealt {round(damage, 2)} damage to {self.player._name}!")
            print(f"{self.player._name} has {round(self.player._hp, 2)} HP left!")
        
    def checkIfFainted(self):
        if self.player._hp <= 0:
            print(self.player._name + " fainted!")
            print("You blacked out!")
            print(f"The opponent's {self.opponent._name} won the battle!")
        elif self.opponent._hp <= 0:
            print(self.opponent._name + " fainted!")
            print(f"The opponent's {self.opponent._name} fainted!")
            print("You won the battle!")

    def addPokemonToPokedex(self, opponentPokemon):
        with open('pokedex.json') as pokedex:
            pokedexFile = json.load(pokedex)

            if opponentPokemon._name not in pokedexFile:
                with open('pokemonList.json') as pokemonList:
                    pokemonData = json.load(pokemonList)

                newPokemon = pokemonData[opponentPokemon._name]
                pokedexFile[opponentPokemon._name] = newPokemon

                try:
                    with open('pokedex.json', 'w') as pokedex:
                        json.dump(pokedexFile, pokedex, indent=4)

                        print(f"{opponentPokemon._name} added to your pokedex!")
                except:
                    print("Error: Unable to add pokemon to pokedex!")
            else:
                print(f"{opponentPokemon._name} already in your pokedex!")


    def fight(self):
        print("\nTrainer Pierce Brosman wants to battle!")
        self.playerPokemonChoice()
        self.opponentPokemonChoice()
        self.player = self.playerPokemon
        self.opponent = self.opponentPokemon
        print("Trainer Pierce Brosman sent out " + self.opponent._name + "!")

        while self.player._hp > 0 and self.opponent._hp > 0:
            self.playerTurn()
            self.opponentTurn()
        
        self.checkIfFainted()
        self.addPokemonToPokedex(self.opponent)

# # TEST CODE
# fight = Fight()
# fight.fight()

