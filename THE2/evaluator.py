# 
# MODIFY get_data() AS YOU LIKE.
# DO NOT SEND THIS FILE TO US

import random
random.seed(111)  #remove hash-sign to get randomization seed we will be using at evaluation
#                    (if you fix the seed you get always the same probabilty choice sequence)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	# @TODO: Update this function just for your own testing. We will use our own get_data().
	       #[M, N,   D,   K, LAMBDA, MU,    universal_state]
	return  [100, 100, 5,  70,  30,  0.50,  [[(12, 18), 5, 'masked', 'infected'] , [(25, 30), 3, 'notmasked', 'infected'] , [(50, 40), 1, 'notmasked', 'notinfected'] , [(66, 10), 7, 'masked', 'notinfected']]]



