# This program is better than gareths version 2.0
import random

def grouppick():
        print('Please input which class you want to play or if you just want to play a random character input random character')
        group = input()

        if group == 'offense':
            offensegroup()

        elif group == 'defense':
                defensegroup()

        elif group == 'tank':
                tankgroup()

        elif group == 'support':
                supportgroup()

        elif group == 'random character':
            charPick()

        else:
            print('Invalid input, please input either "offense", "defense", "tank", "support" or "group character", "random character"')
            grouppick()

def rollAgain():
    print('Would you like to roll again?')
    roll = input()

    if roll == 'yes':
        grouppick()
        

    elif roll == 'no':
        print('Please press enter to exit')
        input()

    else:
        print('Invalid input, please input either "yes" or "no"')
        rollAgain()

def charPick():
    num = random.randint(1,22)
    if num == 1: print ('Your Chracter is Genji')
    if num == 2: print ('Your Chracter is Mccree')
    if num == 3: print ('Your Chracter is Pharah')
    if num == 4: print ('Your Chracter is Reaper')
    if num == 5: print ('Your Chracter is Soldier: 76')
    if num == 6: print ('Your Chracter is Tracer')
    if num == 7: print ('Your Chracter is Bastion')
    if num == 8: print ('Your Chracter is Hanzo')
    if num == 9: print ('Your Chracter is Junkrat')
    if num == 10: print ('Your Chracter is Mei')
    if num == 11: print ('Your Chracter is Torbjorn')
    if num == 12: print ('Your Chracter is Widowmaker')
    if num == 13: print ('Your Chracter is D.VA')
    if num == 14: print ('Your Chracter is Reinhardt')
    if num == 15: print ('Your Chracter is Roadhog')
    if num == 16: print ('Your Chracter is Winston')
    if num == 17: print ('Your Chracter is Zarya')
    if num == 18: print ('Your Chracter is Ana')
    if num == 19: print ('Your Chracter is Lucio')
    if num == 20: print ('Your Chracter is Mercy')
    if num == 21: print ('Your Chracter is Symmetra')
    if num == 22: print ('Your Chracter is Zenyatta')
    print()

    rollAgain()

    grouppick()

def offensegroup():
    offensenum = random.randint(1,6)
    if offensenum == 1: print ('Your character is Genji')
    if offensenum == 2: print ('Your character is Mccree')
    if offensenum == 3: print ('Your character is Pharah')
    if offensenum == 4: print ('Your character is Reaper')
    if offensenum == 5: print ('Your character is Soldier: 76')
    if offensenum == 6: print ('Your character is Tracer')
    print()

    rollAgain()

    grouppick()

def defensegroup():
    defensenum = random.randint(1,6)
    if defensenum == 1: print ('Your character is Bastion')
    if defensenum == 2: print ('Your character is Hanzo')
    if defensenum == 3: print ('Your character is Junkrat')
    if defensenum == 4: print ('Your character is Mei')
    if defensenum == 5: print ('Your character is Torbjorn')
    if defensenum == 6: print ('Your character is Widowmaker')
    print()

    rollAgain()

    grouppick()
 
def tankgroup():
    tanknum = random.randint(1,5)
    if tanknum == 1: print ('Your character is D.VA')
    if tanknum == 2: print ('Your character is Reinhardt')
    if tanknum == 3: print ('Your character is Roadhog')
    if tanknum == 4: print ('Your character is Winston')
    if tanknum == 5: print ('Your character is Zarya')
    print()

    rollAgain()

    grouppick()

def supportgroup():
    supportnum = random.randint(1,5)
    if supportnum == 1: print ('Your character is Ana')
    if supportnum == 2: print ('Your character is Lucio')
    if supportnum == 3: print ('Your character is Mercy')
    if supportnum == 4: print ('Your character is Symmetra')
    if supportnum == 5: print ('Your character is Zenyatta')
    print()

    rollAgain()

    grouppick()

grouppick()

def grouppick():
        print('Please input which class you want to play or if you just want to play a random character input random character')
        group = input()

        if group == 'offense':
            offensegroup()

        elif group == 'defense':
                defensegroup()

        elif group == 'tank':
                tankgroup()

        elif group == 'support':
                supportgroup()

        elif group == 'random character':
            charPick()

        else:
            print('Invalid input, please input either "offense", "defense", "tank", "support" or "group character", "random character"')
            grouppick()
