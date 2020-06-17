#!/usr/bin/python3
""""""
from fighter import Fighter

class Rogue(Fighter):

    def __init__(
        self, name, race, gender, id=None, weapon="daggers", armor="light", champ_class="Rogue",
        health=100, attack=65, defence= 20, magic=10, speed=0, dmg_reduction=0):
        super().__init__(name, race, gender, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)
