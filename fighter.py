#!/usr/bin/python3
""""""
from champ import Champ

class Fighter(Champ):
    def __init__(
        self, name, race, gender, id=None, weapon="sword and shield", armor="heavy", champ_class="Fighter",
        health=100, attack=35, defence= 50, magic=0, speed=0, dmg_reduction=0):
        super().__init__(name, race, gender, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)