import random
from dataclasses import dataclass, field
from typing import List

@dataclass()
class Card:
    name: str
    mana_cost: int
    card_type:str
    attack_power: int
    description: str
    effect_type: str


@dataclass()
class Cards:
    cards: List[Card] = field(default_factory=list)

@dataclass()
class Deck:
    deck: Cards
    hand: int

@dataclass()
class Enemy:
    name: str 
    power: int
    weight: float
    hand: Deck
@dataclass()
class Player:
    name: str
    power: int
    mana: int
    cards: List[Card] = field(default_factory=list)





    





