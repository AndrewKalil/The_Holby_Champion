#!/usr/bin/python3
""""""
from base import Base

class Fighter(Base):
    def __init__(
        self, name, race, gender, id=None, weapon="sword and shield", armor="heavy", champ_class="Fighter",
        health=100, attack=35, defence= 75, magic=0, speed=0, dmg_reduction=0):
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
            self.__speed = 3
        elif self.armor == "medium":
            self.__speed = 7
        elif self.armor == "light":
            self.__speed = 15
        else:
            self.armor = value

    @property
    def dmg_reduction(self):
        return self.__dmg_reduction

    @dmg_reduction.setter
    def dmg_reduction(self, value):
        if self.armor == "heavy":
            self.__dmg_reduction = 6
        elif self.armor == "medium":
            self.__dmg_reduction = 3
        elif self.armor == "light":
            self.__dmg_reduction = 2
        else:
            self.armor = value

    def validator(self, name, value):
        if name is 'name' and len(value) > 10:
            raise Exception("Name is too long, only 10 characters allowed")
        if name is 'race' and (1 > value > 5):
            raise Exception("No race was chosen")
        if name is 'gender' and (1 > value > 3):
            raise Exception("No gender was chosen")

    def __str__(self):
        str = "Class: {}\nName: {}\nRace: {}\nGender: {}\nHealth: {}\nAttack: {}\nDefence: {}\nMagic: {}\nWeapon: {}\nArmor: {}\nSpeed: {}\nDamage Reduction: {}%\nLevel: {}\nEXP for Next Level: {}\nCurrent EXP: {}\nTotal EXP:{}\nChampion id: {}\n"
        return (str.format(
            self.champ_class, self.name, self.race, self.gender, self.health, self.attack, self.defence, self.magic, self.weapon,
            self.armor, self.speed, self.dmg_reduction, self.Level, self.EXP_N_L, self.C_EXP, self.T_EXP, self.id))