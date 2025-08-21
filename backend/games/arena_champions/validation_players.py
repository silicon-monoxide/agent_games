from typing import Dict
import random

from backend.games.arena_champions.player import Player


class HighHealth(Player):

    def __init__(self):
        super().__init__()
        self.strength_p = 0.05
        self.defense_p = 0.05
        self.vitality_p = 0.5
        self.dexterity_p = 0.05
        self.set_to_original_stats()

    def make_combat_decision(
        self,
        opponent_stats: Dict,
        turn: int,
        your_role: str,
        last_opponent_action: str = None,
    ) -> str:
        # Validate role and return appropriate action
        if your_role == "attacker":
            self.add_feedback("Normal attack as attacker")
            return "attack"
        elif your_role == "defender":
            self.add_feedback("Defending with defense")
            return "defend"
        else:
            raise ValueError(
                f"Invalid role: {your_role}. Must be 'attacker' or 'defender'"
            )

class LowHealth1(Player):

    def __init__(self):
        super().__init__()
        self.strength_p = 0.05
        self.defense_p = 0.05
        self.vitality_p = 0.05
        self.dexterity_p = 0.05
        self.set_to_original_stats()

    def make_combat_decision(
        self,
        opponent_stats: Dict,
        turn: int,
        your_role: str,
        last_opponent_action: str = None,
    ) -> str:
        # Validate role and return appropriate action
        if your_role == "attacker":
            self.add_feedback("Normal attack as attacker")
            return "attack"
        elif your_role == "defender":
            self.add_feedback("Defending with defense")
            return "defend"
        else:
            raise ValueError(
                f"Invalid role: {your_role}. Must be 'attacker' or 'defender'"
            )

class LowHealth2(Player):

    def __init__(self):
        super().__init__()
        self.strength_p = 0.05
        self.defense_p = 0.05
        self.vitality_p = 0.06
        self.dexterity_p = 0.05
        self.set_to_original_stats()

    def make_combat_decision(
        self,
        opponent_stats: Dict,
        turn: int,
        your_role: str,
        last_opponent_action: str = None,
    ) -> str:
        # Validate role and return appropriate action
        if your_role == "attacker":
            self.add_feedback("Normal attack as attacker")
            return "attack"
        elif your_role == "defender":
            self.add_feedback("Defending with defense")
            return "defend"
        else:
            raise ValueError(
                f"Invalid role: {your_role}. Must be 'attacker' or 'defender'"
            )

# List of players to be used for validation games
players = [
    HighHealth(),
    LowHealth1(),
    LowHealth2()
]
