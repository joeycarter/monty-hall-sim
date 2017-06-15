# A Monty Hall Simulation

[![Build Status](https://travis-ci.org/joeycarter/monty-hall-sim.svg?branch=master)](https://travis-ci.org/joeycarter/monty-hall-sim)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/joeycarter/monty-hall-sim/blob/master/LICENSE)

The Monty Hall Problem is a simple game of chance whose counterintuitive "solution" has bothered a number of otherwise mathematically literate people I've met over the years.

Here's a short description of the game from [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem):

> Suppose you're on a game show, and you're given the choice of three doors: behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, 'Do you want to pick door No. 2?' The puzzle is, is it to your advantage to switch your choice?

Rules of probability say that players who switch have a 2/3 chance of winning the car, while players who stick to their initial choice have only a 1/3 chance.

I don't doubt that the math checks out, but I wanted a simple simulation to convince myself once and for all that you *are* in fact more likely to win if you switch doors.

## Requirements

* Python 2.6+ or Python 3.3+
* NumPy

## Usage

To run the Python script with default parameters:

    python monty-hall.py

To run e.g. N=10 trials, with verbose output:

    python monty-hall.py -v -N 10

For more information:

    python mony-hall.py --help

## Example

```bash
$ python monty-hall.py -N 100000
```

```
Always changing doors
Running simulation with N = 100000 trials...

Number of wins = 66711
Fraction of games won: 0.66711

----------

Always staying
Running simulation with N = 100000 trials...

Number of wins = 33351
Fraction of games won: 0.33351
```

It works!