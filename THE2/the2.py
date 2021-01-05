#
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() here. Check before submitting

import math
import random
from evaluator import *    # get_data() will come from this import


def new_move():
	# write here your definition. You can also define helper functions




	return get_data()[6:] # @TODO: Change this






def ind_move(last_move,pos):

	if last_move == 0:

		gray= (pos[0],pos[1]-1)
		purple = [(pos[0]+1,pos[1]-1),(pos[0]-1,pos[1]-1)]
		blue = [(pos[0]+1,pos[1]),(pos[0]-1,pos[1])]
		orange = [(pos[0]+1,pos[1]+1),(pos[0]-1,pos[1]+1)]
		green =  (pos[0],pos[1]+1)