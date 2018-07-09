from random import randint

# set min and max values of die
min=1
max=6
#   set a variable roll-again to repeat rolling
roll_again = 'yes'

#  set a number of dice 
number_dice = 1


while roll_again == "yes":
    # integer input to number_dice
    number_dice = int(input("Input the number of dice you want to roll"))
    print("Rolling the dices...")
    print("The values are....")
    while number_dice > 0:
        print(randint(min, max))
        number_dice= number_dice - 1
    
    roll_again = input("Roll the dices again?(yes/no)")




