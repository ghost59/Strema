import random
from dataclasses import dataclass, field
from typing import List
from enum import Enum, auto
from typing import Callable
@dataclass()
class Card:
    name: str
    mana_cost: int
    card_type:str
    attack_power: int
    description: str
    effect_type: str
    effect: Callable

class CardType(Enum):
    ATTACK = auto
    DEFENSE = auto
    SPELL = auto
class CardEffect(Enum):
    NONE = auto
    GROW = auto
    

@dataclass()
class CardState:
    hand: List[Card] = field(default_factory=list)
    decks: List[Card] = field(default_factory=list)
    discard_pile: List[Card] = field(default_factory=list)

@dataclass()
class Enemy:
    name: str 
    power: int
    mana: int
    cards: CardState
@dataclass()
class Player:
    name: str
    power: int
    mana: int
    cards: CardState





    





