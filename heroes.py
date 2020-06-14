#!/usr/bin/python3
""""""
from kamikase import Kamikase


class Heroes(Kamikase):

    def __init__(self, name, race, gender, level, exp_n_l, c_exp, t_exp, id=None):
        self.Name = name
        self.Race = race
        self.Gender = gender
        self.Level = level
        self.EXP_N_L = exp_n_l
        self.C_EXP = c_exp
        self.T_EXP = t_exp
        super().__init__(id)

    def __str__(self):
        str = "Name: {}\n Race: {}\n Gender: {}\n Level: {}\n EXP for Next Level: {}\n Current EXP: {}\n Total EXP: {}\n"
        return (str.format(self.Name, self.Race, self.Gender, self.Level, self.EXP_N_L, self.C_EXP, self.T_EXP))