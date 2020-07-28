import pygame

print (pygame.ver)

'''
The potential idea is to use "states" - when it's the X-person's turn to go, we're in X state, and vice versa. It might be a little extra, but it helps organize a little bit at least. 

The interface will dictate which methods the classes must have (like, check for a win/take a spot)

defaultState will be the starting one (so maybe the players can choose who goes first?)

Possible methods within a state: 

-checkForWin
-addMark (interact with GUI to add X or O)
-retrieveBoard (see which spots are open...? Not sure how we can relay that to backend)

'''