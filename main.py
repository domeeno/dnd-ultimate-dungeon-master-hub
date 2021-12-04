from dice_roller import *
from weapons_parser import get_weapons
from armor_parser import get_armor
import os

def handler(command):
    if command == 'h': # Will be printing the command list. Will add.
        print_command_list()
    elif command == '1': # 1 Dice roll of dice type you want
        roll_simple()
    elif command == '2':
        multiple_roll()
    elif command == 'w':
        get_weapons()
    elif command == 'a':
        get_armor()
    elif command == 'c':
        os.system('clear')

# Results will be printed with double tab
# prompts shows what menu you are
def main():
    prompt = "\ndm>"
    while(True):
        command = input(prompt)
        handler(command)


if __name__ == '__main__':
    print("Welcome Master!")
    main()
