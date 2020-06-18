#!/usr/bin/python3
""""""
from base import Base
import json

class Champ(Base):
    def __init__(
        self, name, race, gender, id=None, weapon="", armor="", champ_class="",
        health=0, attack=0, defence= 0, magic=0, speed=0, dmg_reduction=0):
        self.champ_class = champ_class
        self.name = name
        self.race = race
        self.gender = gender
        self.health = health
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.weapon = weapon
        self.armor = armor
        self.speed = speed
        self.dmg_reduction = dmg_reduction
        super().__init__(id)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validator('name', value)
        self.__name = value

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        self.validator('race', int(value))
        race_list = ["Human", "Elf", "Dwarf", "Hobbit", "Orc"]
        self.__race = str(race_list[int(value) - 1])

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.validator('gender', int(value))
        gender_list = ["Male", "Female", "Other"]
        self.__gender = str(gender_list[int(value) - 1])

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if self.armor == "heavy":
            self.__speed = value + 3
        elif self.armor == "medium":
            self.__speed = value + 7
        elif self.armor == "light":
            self.__speed = value + 15
        else:
            self.__speed = value

    @property
    def dmg_reduction(self):
        return self.__dmg_reduction

    @dmg_reduction.setter
    def dmg_reduction(self, value):
        if self.armor == "heavy":
            self.__dmg_reduction = value + 6
        elif self.armor == "medium":
            self.__dmg_reduction = value + 3
        elif self.armor == "light":
            self.__dmg_reduction = value + 2
        else:
            self.__dmg_reduction = value

    def validator(self, name, value):
        if name is 'name' and len(value) > 10:
            raise Exception("Name is too long, only 10 characters allowed")
        if name is 'race' and (1 > value > 5):
            raise Exception("No race was chosen")
        if name is 'gender' and (1 > value > 3):
            raise Exception("No gender was chosen")

    def __str__(self):
        str = "Class: {}\nName: {}\nRace: {}\nGender: {}\nHealth: {}\nAttack: {}\nDefence: {}\nMagic: {}\nWeapon: {}\nArmor: {}\nSpeed: {}\nDamage Reduction: {}%\nLevel: {}\nEXP for Next Level: {}\nCurrent EXP: {}\nTotal EXP: {}\nStat Points: {}\nChampion id: {}\n"
        return (str.format(
            self.champ_class, self.name, self.race, self.gender, self.health, self.attack, self.defence, self.magic, self.weapon,
            self.armor, self.speed, self.dmg_reduction, self.Level, self.EXP_N_L, self.C_EXP, self.T_EXP, self.S_Points, self.id))

    def to_dictionary(self):
        """turns attributes to a dictionary

        Returns:
            dict: dictionary with all attributes
        """
        dic = {}
        ls = [
            'champ_class', 'name', 'race', 'gender', 'health', 'attack', 'defence', 'magic',
            'weapon', 'armor', 'speed', 'dmg_reduction', 'Level', 'EXP_N_L', 'C_EXP', 'T_EXP', 'S_Points', 'id'
        ]
        for i in ls:
            dic[i] = getattr(self, i)
        return dic

    def save_to_file(self):
        """saves a json string to a file

        Args:
            list_objs (objcet): object to convert to string
        """
        with open("{}.json".format(self.name), mode='w') as fd:
            fd.write(self.to_json_string(self.to_dictionary()))

    def level_up(self):
        self.S_Points += 3
        self.Level += 1
        self.EXP_N_L =  self.EXP_N_L + (self.EXP_N_L * self.Level)
        self.T_EXP += self.C_EXP
        self.C_EXP = 0

    def gain_xp(self, dmg=0):
        self.C_EXP = (0.5 * dmg) + 10

    def death(self):
        self.C_EXP -= (0.5 * self.C_EXP)

    def update(self, **kwargs):
        """udates an object
        """
        for key, value in kwargs.items():
            if key in ['health', 'attack', 'defence', 'magic']:
                value = getattr(self, key) + 3
            elif key in ['speed', 'dmg_reduction']:
                value = getattr(self, key) + .25
            setattr(self, key, value)
        self.S_Points -= len(kwargs)
