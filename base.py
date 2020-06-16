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
