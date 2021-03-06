#!/usr/bin/python3
""""""

from fighter import Fighter
from mage import Mage
from rogue import Rogue
from champ import Champ
from base import Base
from time import sleep

if __name__ == '__main__':

  """dic = Fighter.load_from_file("Andrew")
  p1 = Fighter("Dummy", 1, 1)
  p1.update(**dic)
  p1.level_up()
  p1.increase_stats(health=1, defence=1, armor=1)"""
  """
  p1 = Mage("Andrew", "Human", "Male", "Solar")
  p1.update(Level=10)
  print(p1, end="\n")
  print(p1.attack_action())
  print(p1.soul_burn("Arc"))
  print(p1.legion_attack("Arc"))
  print(p1.ultimate("Arc"))
  print()
  print(p1.attack_action())
  print(p1.soul_burn())
  print(p1.legion_attack())
  print(p1.ultimate())

  p2 = Mage("Adrian", "Human", "Male", "Solar")
  p2.update(Level=10)
  print(p2, end="\n")
  print(p2.attack_action())
  print(p2.soul_burn("Arc"))
  print(p2.legion_attack("Arc"))
  print(p2.ultimate("Arc"))
  print()
  print(p2.attack_action())
  print(p2.soul_burn())
  print(p2.legion_attack())
  print(p2.ultimate())
  """
  """p1.save_to_file()"""
  p1 = Fighter("Andrew", 1, 1)
  p2 = Rogue("Sasuke", 2, 1)
  print(p1, end="\n")
  print(p2, end="\n")

while True:
    if p1.health <= 0 or p2.health <= 0:
      if p1.health > 0:
        print("PLAYER 1 WINS")
        p1.win()
        p2.lose()
      elif p2.health > 0:
        print("PLAYER 2 WINS")
        p2.win()
        p1.lose()
      break

    if p1.health > 0:
      print("Player 1 Attacking...")
      sleep(3)
      dmg1 = p1.attack_action()
      p2.defend_action(dmg1)
      print("Player 1 stats after attack:")
      p1.display_battle_stats()
      print("Player 2 stats after attack")
      p2.display_battle_stats()

    if p2.health > 0:
      print("Player 2 Attacking...")
      sleep(3)
      dmg2 = p2.attack_action()
      p1.defend_action(dmg2)
      print("Player 1 stats after attack:")
      p1.display_battle_stats()
      print("Player 2 stats after attack")
      p2.display_battle_stats()
