from pokemon import *
import random
from typing import List

class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()

    def __init__(self):
        self.team = []

    def choose_manually(self):
        for i in range(self.TEAM_LIMIT):
            choice = input("Enter the name of the Pokemon (or leave blank to finish): ").strip()
            if choice:
                self.team.append(choice)
            else:
                break

    def choose_randomly(self) -> None:
        self.team = random.sample(self.POKE_LIST, min(len(self.POKE_LIST)), self.TEAM_LIST))

    def regenerate_team(self, battle_mode, criterion=None) -> None:
        for pokemon in self.team:
            pokemon.reset_health()

        #Assemble the team based on bettle mode
        if battle_mode == "FRONT":
            #Logic for FRONT mode: Keep the current order of Pokemon in the team
            pass
        elif battle_mode == "BACK":
            #Logic for BACK mode: Reverse the order of Pokemon in the team
            self.team = self.team[::-1}
        elif battle_mode == "OPTIMISE":
            # Logic for OPTIMISE mode: Sort the team based on a specific criterion
            if criterion == "level":
                self.team.sort(key=lambda x: x.get_level(), reverse=True)
            elif criterion == "health":
                self.team.sort(key=lambda x: x.get_health(), reverse=True)
            #Add more criteria as needed
        else:
            raise ValueError("Invalid battle mode.")

    def __getitem__(self, index: int):
        return self.team[index]

    def __len__(self):
        return len(self.team)

    def __str__(self):
        return '\n'.join(self.team)

class Trainer:

    def __init__(self, name) -> None:
        self.name = name
        self.poke_team = PokeTeam()
        self.pokedex = set()

    def pick_team(self, method: str) -> None:
        if method == "Random":
            self.poke_team.choose_randomly()
        elif method == "Manual":
            self.poke_team.choose_manually()
        else:
            raise ValueError("Invalid team selection method.")

    def get_team(self) -> PokeTeam:
        return self.poke_team

    def get_name(self) -> str:
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        self.pokedex.add(pokemon.get_poketype())

    def get_pokedex_completion(self) -> float:
        completion = len(self.pokedex) / len(PokeType)
        return round(completion * 100, 2)

    def __str__(self) -> str:
        return f"Trainer {self.name} Pokedex Completion: {self.get_pokedex_completion()%"

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
