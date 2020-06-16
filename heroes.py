#!/usr/bin/python3
""""""
class Base():
    EXP_N_L = 10
    C_EXP = 0
    T_EXP = 0
    Level = 0
    nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.nb_object += 1
            self.id = Base.nb_object
        self.C_EXP = Base.C_EXP
        self.T_EXP = Base.T_EXP
        self.Level = Base.Level
        self.EXP_N_L = Base.EXP_N_L

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

    def validator(self, name, value):
        if name is 'name' and len(value) > 10:
            raise Exception("Name is too long, only 10 characters allowed")
        if name is 'race' and (1 > value > 5):
            raise Exception("No race was chosen")
        if name is 'gender' and (1 > value > 3):
            raise Exception("No gender was chosen")

    def __str__(self):
        str = "Name: {}\nRace: {}\nGender: {}\nLevel: {}\nEXP for Next Level: {}\nCurrent EXP: {}\nTotal EXP:{}\nChampion id: {}\n"
        return (str.format(self.name, self.race, self.gender, self.Level, self.EXP_N_L, self.C_EXP, self.T_EXP, self.id))