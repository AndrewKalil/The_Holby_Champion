#!/usr/bin/python3

from champ import Champ


class Battle():
    def __init__(self, Heroe_1, Heroe_2):
        self.Heroe_1 = Heroe_1
        self.Heroe_2 = Heroe_2
        self.current_turn = 0
    
    def is_finished(self):
        finished = self.Heroe_1.current_hp <= 0 or self.Heroe_2.current_hp <= 0
        if finished:
            self.print_winner()
        return finished

    def print_winner(self):
        if self.Heroe_1.current_hp <= 0 < self.Heroe_2.current_hp:
            print(self.Heroe_2.name + "Won in" +str(self.current_turn)+" Turns!!")
        elif self.Heroe_2.current_hp <= 0 < self.Heroe_1.current_hp:
            print(self.Heroe_1.name + " won in " + str(self.current_turn)+" turns!!")
        else:
            print("DOUBLE KO")


    def execute_turn(self, turn):
        attack1 = None
        attack2 = None
        self.Heroe_1.health -= attack1.attack
        self.Heroe_2.health -= attack2.attack
        self.current_turn += 1

    def print_current_status(self):
        print(self.Heroe_1.Name + "has" + str(self.Heroe_1.current_hp) + " left")
        print(self.Heroe_2.Name + "has" + str(self.Heroe_2.current_hp) + " left")

class Attack(Champ):
    def __init__(self):
        super().__init__(id)

class Turn():
    def __init__(self):
        self.argv1 = None
        self.argv2 = None

    def can_start(self): 
        return self.argv1 is not None and self.argv2 is not None

class Command():
    def __init__(self, action):
        self.action = action