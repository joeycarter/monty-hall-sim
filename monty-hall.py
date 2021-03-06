# Copyright (c) 2017 Joey Carter
#
# See the file "LICENSE" for information on the terms & conditions for usage of
# this software.

"""
A Monty Hall Simulation

"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import argparse
import warnings
import numpy as np


def trial(car, initial, change, verbose=False):
    """Perform the simulation of one trial

    Parameters
    ----------
    car : int
        The door the car is behind (1, 2 or 3)
    initial : int
        The player's initial door selection (1, 2 or 3)
    change : bool
        If true, the player will change their selection when asked
    verbose : bool
        If true, print additional information

    Returns
    -------
    bool
        True if the player wins, False if they lose
    """

    if verbose:
        print('Player chooses door ' + str(initial) +
              ' (car behind door ' + str(car) + ')')

    # Player guesses; reveal a door with a goat behind it
    if car == initial:
        # Player guessed correctly; open either of the other doors
        reveal = rand_exclude(car)
    else:
        # Player guessed incorrectly; open the other goat door
        reveal = exclude(car, initial)

    if verbose:
        print('Door ' + str(reveal) + ' is revealed')

    if change:
        final = exclude(reveal, initial)
        if verbose:
            print('Player decides to change to door ' + str(final))
    else:
        final = initial
        if verbose:
            print('Player stays with door ' + str(final))

    # Check if they won
    if car == final:
        win = True
        if verbose:
            print('Player wins!\n')
    else:
        win = False
        if verbose:
            print('Player loses!\n')

    return win


def rand_exclude(ex):
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
        raise Exception('rand_exclude only works for 1, 2, 3')


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


def run_trials(N, change, verbose):
    """Run N trials, either always changing doors, or always staying

    Parameters
    ----------
    N : int
        Number of trials
    change : bool
        If True, change doors, otherwise stay
    verbose : bool
        If true, print additional information
    """

    if change:
        print('Always changing doors')
    else:
        print('Always staying')

    print('Running simulation with N = ' + str(N) + ' trials...\n')

    # Randomly assign which door the car is behind (1, 2 or 3)
    cars = np.random.randint(1, 4, size=N)

    # Randomly set the player's initial door selection (1, 2 or 3)
    initials = np.random.randint(1, 4, size=N)

    nWins = 0

    for i in range(0, N):
        win = trial(cars[i], initials[i], change, verbose)

        if win:
            nWins += 1

    print('Number of wins = ' + str(nWins))

    # Calculate stats
    fracWon = nWins / N

    print('Fraction of games won: ' + str(fracWon))


def main():
    # Parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="verbose output")
    parser.add_argument("-N", "--ntrial", type=int, default=100,
                        help="number of trials to run")
    args = parser.parse_args()

    # Number of trials
    N = args.ntrial

    if args.verbose and N >= 200:
        warnings.warn("This will produce a lot of output!")
        input("Press Enter to continue...")

    # Run the simulation; always change doors
    run_trials(N, True, args.verbose)

    print('\n----------\n')

    # Run the simulation; always stay
    run_trials(N, False, args.verbose)


if __name__ == '__main__':
    main()
