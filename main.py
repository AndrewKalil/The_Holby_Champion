#!/usr/bin/python3
""""""

from fighter import Fighter
from mage import Mage
from rogue import Rogue
from champ import Champ
from battle import Battle, Turn
import os

if __name__ == '__main__':
  champ_class = 1
  name = "Pekka"
  race = 1
  gender = 2

  champ_class = 2
  name2 = "Merlin"
  race2 = 1
  gender2 = 2

  champ_class = int(champ_class)
  if champ_class is 1:
    func = Fighter
  elif champ_class is 2:
    func = Mage
  elif champ_class is 3:
    func = Rogue

  os.system("clear")
  h1 = func(name, race, gender)
  print(h1, end="\n")

  h2 = func(name2, race2, gender2)
  print(h2, end='\n')

  battle = Battle(h1, h2)

  while not battle.is_finished():
    turn = Turn()
    turn.Heroe_1
    turn.Heroe_2

    if turn.can_start():
      battle.execute_turn(turn)
      battle.print_current_status()
  """
  h1.level_up()
  print(h1, end="\n")
  h1.update(speed=1, dmg_reduction=1, attack=1)
  print(h1, end="\n")"""



