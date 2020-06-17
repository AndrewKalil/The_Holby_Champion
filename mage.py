#!/usr/bin/python3
""""""
from fighter import Fighter

class Mage(Fighter):

    def __init__(
        self, name, race, gender, id=None, weapon="staff", armor="medium", champ_class="Mage",
        health=100, attack=0, defence= 35, magic=65, speed=0, dmg_reduction=0):
        super().__init__(name, race, gender, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)