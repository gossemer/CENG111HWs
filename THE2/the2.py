import math
import random
from evaluator import *    # get_data() will come from this import


last_move_table=[[0 , 1],
				 [-1, 1],
				 [-1, 0],
				 [-1,-1],
				 [0 ,-1],
				 [1 ,-1],
				 [1 , 0],
				 [1 , 1]]

def ind_move(lm,pos,table,mu):
	
	f_fwd = table[lm]
	l_fwd = table[lm-1]
	left  = table[lm-2]
	l_bwd = table[lm-3]
	f_bwd = table[lm-4]
	r_bwd = table[lm-5]
	right = table[lm-6]
	r_fwd = table[lm-7]
	new_move = random.choices([f_fwd,r_fwd,right,r_bwd,f_bwd,l_bwd,left,l_fwd],
							[mu/2,mu/8,(1-mu-mu**2)/2,2*mu**2/5,mu**2/5,2*mu**2/5,(1-mu-mu**2)/2,mu/8])[0]

	for i in range(len(table)):
		if table[i] == new_move:
			lm = i
	return (pos[0]+new_move[0],pos[1]+new_move[1]),lm



def is_occupied(universal_state,pot_pos):
	for i in universal_state:
		if i[0] == pot_pos:
			return True
	return False

def transmition(D,K,lmb,p1,p2):
	distance12 = math.sqrt((p1[0][0]-p2[0][0])**2+(p1[0][1]-p2[0][1])**2)
	if D < distance12 or p2[3] == p1[3] or (p1[3] == 'transmitted' and p2[3]== 'notinfected') or (p1[3] == 'notinfected' and p2[3]== 'transmitted'):
		return p1,p2
	mask_factor = 1
	if p1[2] == 'masked':
		mask_factor *= lmb
	if p2[2] == 'masked':
		mask_factor *= lmb
	prob = min(1,K/(distance12**2))
	prob /= mask_factor
	is_transmitted = random.choices([1,0],[prob,1-prob])[0]
	
	if is_transmitted:
		if p1[3] == 'notinfected':
			p1[3] ='transmitted'
		elif p2[3] == 'notinfected': 
			p2[3] ='transmitted'
	return p1,p2

M,N,D,K,lmb,mu,universal_state = get_data()
def new_move():
	global M,N,D,K,lmb,mu,universal_state
	for i in universal_state:
		pot_pos = ind_move(i[1],i[0],last_move_table,mu)

		if 0<=pot_pos[0][0]<N and 0<= pot_pos[0][1] < M and (not is_occupied(universal_state,pot_pos[0])):
			i[0],i[1] = pot_pos
		
	for i in range(len(universal_state)):
		for j in range(i+1,len(universal_state)):
			universal_state[i],universal_state[j] = transmition(D,K,lmb,universal_state[i],universal_state[j])
	
	for p in universal_state:
		if p[3] == 'transmitted':
			p[3] = 'infected'
	return universal_state
