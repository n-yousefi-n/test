#barname sang - khaghaz - gheychi
import sys
import random
from enum import Enum
class RPS(Enum):
    sang = 1
    kakhz = 2
    qaichi = 3
while True :
    player_choice = int(input("enter...\n 1 for sang \n 2 for kakhz \n 3 for qaichi \n "))
    if player_choice <1 or player_choice >3:
        sys.exit("enter must a 1 , 2 , 3 :")
    com_choice = int(random.choice("123"))
    print("."*30)
    print(f"player choice is = {str(RPS(player_choice)).replace('RPS.','')}.")
    print(f"pc choice is =  {str(RPS(com_choice)).replace('RPS.','')}.")
    print("."*30)
    if player_choice == 3 and com_choice == 1 or player_choice == 2 and com_choice == 1  or player_choice == 2 and com_choice == 3 :
        print("you lose !")
    elif player_choice == 3 and com_choice == 2 or player_choice == 1 and com_choice == 2 or player_choice == 1 and com_choice == 3 :
        print("you won !")
    if player_choice == com_choice :
        print("you are equal")
    print("."*30)