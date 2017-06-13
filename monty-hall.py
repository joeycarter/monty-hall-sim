import numpy as np

# Number of trials
N = 100000

# Door the car is behind (1, 2, 3)
cars = np.random.randint(1, 4, size=N)

# Player's initial selection (1, 2, 3)
initSels = np.random.randint(1, 4, size=N)


def trial(car, initSel, change):
	# print('Player chooses door ' + str(initSel) + ' (car behind door ' + str(car) + ')')

	# Open one of the doors without a car
	tmp = np.random.randint(2)

	# Player guesses; reveal a door with a goat behind it
	if car == initSel:
		# Player guessed correctly; open either of the other doors
		reveal = randExclude(car)
	else:
		# Player guessed incorrectly; open the other goat door
		reveal = exclude(car, initSel)

	# print('Door ' + str(reveal) + ' is revealed')

	if change:
		finalSel = exclude(reveal, initSel)
		# print('Player decides to change to door ' + str(finalSel))
	else:
		finalSel = initSel
		# print('Player stays with door ' + str(finalSel))

	# Check if they won
	if car == finalSel:
		win = 1
		# print('Player wins!\n')
	else:
		win = 0
		# print('Player looses!\n')

	return win


def randExclude(ex):
	"""Generate a random number on interval [1,3], excluding 'ex'
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
	"""

	if (ex1 == 1 and ex2 == 2) or (ex1 == 2 and ex2 == 1):
		return 3
	elif (ex1 == 1 and ex2 == 3) or (ex1 == 3 and ex2 == 1):
		return 2
	elif (ex1 == 2 and ex2 == 3) or (ex1 == 3 and ex2 == 2):
		return 1
	else:
		raise Exception('exclude only works for 1, 2, 3')

# Run N trials

nWins = 0

for i in range(0, N):
	win = trial(cars[i], initSels[i], 1)
	
	if win:
		nWins += 1

print('N = ' + str(N) + ', N wins = ' + str(nWins))

# Calculate stats
fracWon = nWins / N

print('Fraction of games won: ' + str(fracWon))
