from random import randrange

dice_prompt = '\ndice'

def roll_simple():
    done = False
    while(not done):
        dice = input(dice_prompt + " type>")
        try:
            val = int(dice)
            roll = randrange(val)
            print("D" + str(val) + " rolled: " + str(roll))
            done = True
        except ValueError:
            if dice == 'q':
                done = True
            else:
                print("Can't do that")

def multiple_roll():
    done = False
    while(not done):
        number_of_dices = input(dice_prompt + " number>")
        dice = input(dice_prompt + " type>")
        try:
            val = int(dice)
            size = int(number_of_dices)
            rolls = []
            for i in range(size):
                roll = randrange(val)
                rolls.append(roll)
            print("D" + str(val) + " rolled: ")
            print(rolls)
            done = True
        except ValueError:
            if dice == 'q' or number_of_dices == 'q':
                done = True
            else:
                print("Can't do that")
