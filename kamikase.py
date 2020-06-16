#!/usr/bin/python3

""""""
import time
import sys


class Kamikase():
    """Kamikase main Class"""
    EXP_N_L = 10
    C_EXP = 0
    T_EXP = 0
    Level = 0
    nb_object = 0

    def __init__(self, id = None):

        if id is not None:
            self.id = id
        else:
            Kamikase.nb_object += 1
        self.id = Kamikase.nb_object
        self.C_EXP = Kamikase.C_EXP
        self.T_EXP = Kamikase.T_EXP
        self.Level = Kamikase.Level
        self.EXP_N_L = Kamikase.EXP_N_L



"""

def print_slow(s):
    for c in s:
        sys.stout.write(c)
        sys.stout.flush()
        time.sleep(0.08)
"""