#!/usr/bin/python3
""""""
from champ import Champ

class Rogue(Champ):

    def __init__(
        self, name, race, gender, id=None, weapon="daggers", armor="light", champ_class="Rogue",
        health=100, attack=65, defence= 20, magic=0, speed=0, dmg_reduction=0):
        super().__init__(name, race, gender, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)
