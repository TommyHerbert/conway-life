# exercise 1.4b
# use a hat to stabilize one side of the twin bees shuttle

import glife, golly
from search import spiral

block = glife.pattern('2o$2o!')
b_heptomino = glife.pattern('o$2o$b2o$2o!')
domino = glife.pattern('2o!')
bee_with_domino = domino(0, 3) + b_heptomino(4, 0)
bee_domino_block = bee_with_domino + block(14, 1)
bees = bee_with_domino + bee_with_domino(0, 10, glife.flip_y)
partial_shuttle = bees + block(14, 1)
shuttle = partial_shuttle + block(-13, 1)
shuttle.display()

hat = pattern('2bo$bobo$bobo$2ob2o!')

searching = True
position = spiral(-13, 1)

while searching:
	x, y = next(position)
	candidate = partial_shuttle + hat(x, y)
	candidate.display()
	hash_value = golly.hash(golly.getrect())
	candidate.evolve(46)
	candidate.display
	if golly.hash(golly.getrect()) == hash_value:
		searching = False
