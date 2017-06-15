"""monty-hall.py

Author: Joey Carter

"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import argparse
import numpy as np
import warnings

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
parser.add_argument("-N", "--ntrial", type=int, default=100, help="number of trials to run")
args = parser.parse_args()

# Number of trials
N = args.ntrial

if args.verbose and N >= 200:
    warnings.warn("This will produce a lot of output!")
    input("Press Enter to continue...")


def trial(car, initSel, change):
    """Perform the simulation of one trial

    Parameters
    ----------
    car : int
        The door the car is behind (1, 2 or 3)
    initSel : int
        The player's initial door selection (1, 2 or 3)
    change : bool
        If true, the player will change their selection when asked

    Returns
    -------
    bool
        True if the player wins, False if they lose
    """

    if args.verbose:
        print('Player chooses door ' + str(initSel) +
              ' (car behind door ' + str(car) + ')')

    # Player guesses; reveal a door with a goat behind it
    if car == initSel:
        # Player guessed correctly; open either of the other doors
        reveal = randExclude(car)
    else:
        # Player guessed incorrectly; open the other goat door
        reveal = exclude(car, initSel)

    if args.verbose:
        print('Door ' + str(reveal) + ' is revealed')

    if change:
        finalSel = exclude(reveal, initSel)
        if args.verbose:
            print('Player decides to change to door ' + str(finalSel))
    else:
        finalSel = initSel
        if args.verbose:
            print('Player stays with door ' + str(finalSel))

    # Check if they won
    if car == finalSel:
        win = True
        if args.verbose:
            print('Player wins!\n')
    else:
        win = False
        if args.verbose:
            print('Player looses!\n')

    return win


def randExclude(ex):
    """Generate a random number on interval [1,3], excluding 'ex'

    Parameters
    ----------
    ex : int
        The number to exclude (1, 2 or 3)

    Returns
    -------
    int
        The random number
    """

    tmp = np.random.randint(2)

    if ex == 1:
        if tmp == 0:
            return 2
        else:
            return 3
    elif ex == 2:
        if tmp == 0:
            return 1
        else:
            return 3
    elif ex == 3:
        if tmp == 0:
            return 1
        else:
            return 2
    else:
        raise Exception('randExclude only works for 1, 2, 3')


def exclude(ex1, ex2):
    """Return the number on the interval [1,3] that is neither ex1 nor ex2

    Parameters
    ----------
    ex1 : int
        The first number to exclude (1, 2 or 3)
    ex2 : int
        The second number to exclude (1, 2 or 3)

    Returns
    -------
    int
        The number (1, 2 or 3) not excluded
    """

    if (ex1 == 1 and ex2 == 2) or (ex1 == 2 and ex2 == 1):
        return 3
    elif (ex1 == 1 and ex2 == 3) or (ex1 == 3 and ex2 == 1):
        return 2
    elif (ex1 == 2 and ex2 == 3) or (ex1 == 3 and ex2 == 2):
        return 1
    else:
        raise Exception('exclude only works for 1, 2, 3')


def runTrials(change):
    """Run N trials, either always changing doors, or always staying

    Parameters
    ----------
    change : bool
        If True, change doors, otherwise stay
    """

    if change:
        print('Always changing doors')
    else:
        print('Always staying')

    print('Running simulation with N = ' + str(N) + ' trials...\n')

    # Randomly assign which door the car is behind (1, 2 or 3)
    cars = np.random.randint(1, 4, size=N)

    # Randomly set the player's initial door selection (1, 2 or 3)
    initSels = np.random.randint(1, 4, size=N)

    nWins = 0

    for i in range(0, N):
        win = trial(cars[i], initSels[i], change)

        if win:
            nWins += 1

    print('Number of wins = ' + str(nWins))

    # Calculate stats
    fracWon = nWins / N

    print('Fraction of games won: ' + str(fracWon))


# Run the simulation; always change doors
runTrials(True)

print('\n----------\n')

# Run the simulation; always stay
runTrials(False)
