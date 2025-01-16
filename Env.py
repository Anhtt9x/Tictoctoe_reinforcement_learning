import numpy as np
import random
from itertools import groupby , product

class TicTacToe:
    def __init__(self):
        self.state = [np.nan for _ in range(9)]
        self.all_possible_number = [i for i in range(1,len(self.state)+1)]
        self.reset()

    def reset(self):
        return self.state

    def is_winning(self, curr_state):
        win_sum = 15
        if ((curr_state[0] + curr_state[1] + curr_state[2]) ==  win_sum) or \
            ((curr_state[3] + curr_state[4] + curr_state[5]) == win_sum) or \
            ((curr_state[6] + curr_state[7] + curr_state[8]) == win_sum) or \
            ((curr_state[0] + curr_state[3] + curr_state[6]) == win_sum) or \
            ((curr_state[1] + curr_state[4] + curr_state[7]) == win_sum) or \
            ((curr_state[2] + curr_state[5] + curr_state[8]) == win_sum) or \
            ((curr_state[0] + curr_state[4] + curr_state[8]) == win_sum) or \
            ((curr_state[2] + curr_state[4] + curr_state[6]) == win_sum):
            return True
        else:
            return False
        
    def is_terminal(self,curr_state):
        if self.is_winning(curr_state):
            return True,"Win"
        elif len(self.allowed_positions(curr_state))==0:
            return True, "Tie"
        else:
            return False,"Continue"


    def allowed_positions(self,curr_state):
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]
    
    
    def allowed_values(self,curr_state):
        used_value = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_number if val not in used_value and val%2 !=0]
        

