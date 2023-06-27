from glife import *
twinbees = pattern('4bo$4b2o8b2o$5b2o7b2o$2o2b2o4$2o2b2o$5b2o7b2o$4b2o8b2o$4bo!')
twinbees.put(14,2)
hat = pattern('2bo$bobo$bobo$2ob2o!')
hat.put(1,3)

"""
start with a twin bees shuttle minus the blocks on the right-hand side
put a hat roughly where one of the blocks would have been
go forward n generations, where n is the period of the twin bees shuttle
if the pattern is the one you started with, stop
otherwise, slightly move the hat and try again
keep doing this until the right position is found
the hat should move in a spiral pattern, outwards from where it starts

next I need to start reading some scripts and the docs to work out how to do these steps
"""
