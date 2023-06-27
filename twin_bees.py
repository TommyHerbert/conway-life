# exercise 1.4b
# use a hat to stabilize one side of the twin bees shuttle

import glife, golly

block = glife.pattern('2o$2o!')
b_heptomino = glife.pattern('o$2o$b2o$2o!')
domino = glife.pattern('2o!')
bee_with_domino = domino(0, 3) + b_heptomino(4, 0)
bee_domino_block = bee_with_domino + block(14, 1)
bees = bee_with_domino + bee_with_domino(0, 10, glife.flip_y)
partial_shuttle = bees + block(14, 1)
shuttle = partial_shuttle + block(-13, 1)
shuttle.display()
