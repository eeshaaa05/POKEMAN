from enum import Enum
from queue_adt import ArrayQueue, Queue
from pokemon import Pokemon

class BattleMode(Enum):
    SET = 0
    ROTATE = 1
    OPTIMISE = 2

class Battle:
    def __init__(self, battle_mode: BattleMode):
        self.battle_mode = battle_mode
        self.battle_queue: Queue = ArrayQueue(max_capacity=6)
        self.order_attribute = None  # Attribute chosen for optimized mode ordering

    def add_pokemon(self, pokemon: Pokemon):
        """Add a Pokemon to the battle queue."""
        if len(self.battle_queue) < 6:
            self.battle_queue.enqueue(pokemon)
        else:
            raise Exception("Battle queue is full")

    def start_battle(self):
        """Start the battle based on the selected battle mode."""
        if self.battle_mode == BattleMode.SET:
            self.start_set_mode_battle()
        elif self.battle_mode == BattleMode.ROTATE:
            self.start_rotate_mode_battle()
        elif self.battle_mode == BattleMode.OPTIMISE:
            self.start_optimise_mode_battle()
        else:
            raise ValueError("Invalid battle mode selected")

    def start_set_mode_battle(self):
        """Start the battle in Set mode."""
        while not self.battle_queue.is_empty():
            current_pokemon = self.battle_queue.peek()
            print(f"{current_pokemon.get_name()} is attacking!")
            opponent_fainted = self.simulate_attack(current_pokemon)
            if opponent_fainted:
                self.battle_queue.dequeue()
            else:
                print(f"{current_pokemon.get_name()} continues the battle!")
        print("All Pokémon in the battle queue have been defeated. Battle over.")

    def start_rotate_mode_battle(self):
        """Start the battle in Rotate mode."""
        while not self.battle_queue.is_empty():
            current_pokemon = self.battle_queue.peek()
            print(f"{current_pokemon.get_name()} is attacking!")
            opponent_fainted = self.simulate_attack(current_pokemon)
            if opponent_fainted:
                self.battle_queue.dequeue()
            else:
                self.rotate_team()
        print("All Pokémon in the battle queue have been defeated. Battle over.")

    def start_optimise_mode_battle(self):
        """Start the battle in Optimise mode."""
        if self.order_attribute is None:
            raise ValueError("Order attribute not specified for Optimise mode")
        self.assign_team()
        self.start_set_mode_battle()  # Optimised mode is essentially Set mode with custom ordering

    def simulate_attack(self, current_pokemon: Pokemon) -> bool:
        """Simulate a single attack."""
        opponent = self.battle_queue.peek()
        damage = self.calculate_damage(current_pokemon, opponent)
        opponent.defend(damage)
        print(f"{opponent.get_name()} received {damage} damage.")
        if not opponent.is_alive():
            print(f"{opponent.get_name()} fainted!")
            return True
        return False

    def calculate_damage(self, attacker: Pokemon, defender: Pokemon) -> int:
        """Calculate the damage inflicted by the attacker on the defender."""
        # Placeholder damage calculation based on attacker's battle power
        damage = attacker.get_battle_power()
        return damage

    def rotate_team(self):
        """Rotate the team by moving the front Pokemon to the back."""
        front_pokemon = self.battle_queue.dequeue()
        self.battle_queue.enqueue(front_pokemon)

    def assign_team(self):
        """Assign order to the team based on the chosen attribute."""
        if self.order_attribute == "Level":
            # Sort team by level
            self.battle_queue.items.sort(key=lambda x: x.get_level(), reverse=True)
        elif self.order_attribute == "HP":
            # Sort team by HP
            self.battle_queue.items.sort(key=lambda x: x.get_health(), reverse=True)
        elif self.order_attribute == "Attack":
            # Sort team by attack power
            self.battle_queue.items.sort(key=lambda x: x.get_battle_power(), reverse=True)
        elif self.order_attribute == "Defence":
            # Sort team by defence
            self.battle_queue.items.sort(key=lambda x: x.get_defence(), reverse=True)
        elif self.order_attribute == "Speed":
            # Sort team by speed
            self.battle_queue.items.sort(key=lambda x: x.get_speed(), reverse=True)
        else:
            raise ValueError("Invalid order attribute specified for Optimise mode")
