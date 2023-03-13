import json
import random

with open('pokemonList.json') as pokemonList:
    pokemon = json.load(pokemonList)

with open('pokedex.json') as pokedex:
    pokedexFile = json.load(pokedex)

with open('pokemonMove.json') as attack:
    attackList = json.load(attack)

with open('pokemonEffect.json') as typeEffectiveness:
    attackEffect = json.load(typeEffectiveness)

class Pokemon:
    def __init__(self, name):
        # GENERAL POKEMON ATTRIBUTES #
        self._name = name
        self.pokedexNumber = pokemon[name]['pokedexId']
        self.type = pokemon[name]['type']
        self.level = pokemon[name]['level']
        self.exp = pokemon[name]['experience']
        self.specie = pokemon[name]['species']
        self.height = pokemon[name]['height']
        self.weight = pokemon[name]['weight']

        # BASE STATS #
        # self.move = pokemon[name]['moves']

        # self.move = random.sample(pokemon[name]['moves'], 4)
        moves = pokemon[name]['moves']
        self.move = [moves[i] for i in random.sample(range(len(moves)), min(4,len(moves)))]
        self._hp = pokemon[name]["baseStats"]['hp']
        self.attack = pokemon[name]["baseStats"]['attack']
        self.defense = pokemon[name]["baseStats"]['defense']
        self.attackSp = pokemon[name]["baseStats"]['specialAttack']
        self.defenseSp = pokemon[name]["baseStats"]['specialDefense']
        self.speed = pokemon[name]["baseStats"]['speed']

        # IVS #
        self._hpIV = pokemon[name]["ivs"]['hp']
        self.attackIV = pokemon[name]["ivs"]['attack']
        self.defenseIV = pokemon[name]["ivs"]['defense']
        self.attackSpIV = pokemon[name]["ivs"]['specialAttack']
        self.defenseSpIV = pokemon[name]["ivs"]['specialDefense']
        self.speedIV = pokemon[name]["ivs"]['speed']

        
    def __str__(self):
        return (
            f"\nGeneral Pokemon Info:"
            f"\nName: {self._name}"
            f"\nPokedex Number: {self.pokedexNumber}"
            f"\nType: {self.type}"
            f"\nSpecie: {self.specie}"
            f"\nHeight: {self.height}"
            f"\nWeight: {self.weight}"
            f"\n_______________________________________________________"
            f"\n\nBase Stats:"
            f"\nMoves Learned: {self.move}"
            f"\nLevel: {self.level}"
            f"\nExperience: {self.exp}"
            f"\nHP: {self._hp}"
            f"\nAttack: {self.attack}"
            f"\nDefense: {self.defense}"
            f"\nSpecial Attack: {self.attackSp}"
            f"\nSpecial Defense: {self.defenseSp}"
            f"\nSpeed: {self.speed}"
        )
    
    def getHealth(self):
        print(f"{self._name} has {self._hp} HP left!")
        return self._hp
    
    
    def performAttack(self, opponent, moveName):
        if moveName not in self.move:
            print("This Pokemon does not know this move!")
            return 
        
        moveDetails = attackList[moveName]
        power = moveDetails['power']
        accuracy = moveDetails['accuracy']
        moveType = moveDetails['type']

        if accuracy < random.randint(0,100):
            print(f"{self._name}'s {moveName} missed!")
            return 0.0
        
        missChance = opponent.speed / self.speed * 100
        if missChance > 255:
            missChance = 255

        #critChance = self.speed / (2 * opponent.speed) * 100
        critChance = 1 / 16

        isCriticalHit = False
        if random.randint(1, 100) <= critChance * 100:
            isCriticalHit = True

        if isCriticalHit:
            level = self.level * 2
        else:
            level = self.level

        effectiveness = 1.0
        for t in opponent.type:
            if t in attackEffect[moveType]["weaknesses"]:
                effectiveness *= 2.0
            elif t in attackEffect[moveType]["strengths"]:
                effectiveness *= 0.5

        STAB = 1.5 if moveType in self.type else 1.0

        computedAttack = self.attack
        computedDefense = opponent.defense
        if isCriticalHit:
            computedAttack = ((self.attack * 2) + self.attackIV) // 100
            computedDefense = ((opponent.defense * 2) + opponent.defenseIV) // 100
            
        else:
            computedAttack = ((self.attack * 2) + self.attackIV) // 100
            computedDefense = ((opponent.defense * 2) + opponent.defenseIV) // 100

        damage = (((((2 * level) / 5) + 2) * power * (computedAttack / computedDefense)) // 50) + 2 * STAB * effectiveness * random.randint(85, 100) / 100


        damage = int(damage)
        if damage == 0:
            print("It has no effect!")
        else:
            opponent._hp -= damage
            print(f"{opponent._name} took {damage} damage!")

            if isCriticalHit:
                print("Critical Hit!")
            if effectiveness > 1:
                print("It's super effective!")
            elif effectiveness < 1:
                print("It's not very effective!")

        return damage   


