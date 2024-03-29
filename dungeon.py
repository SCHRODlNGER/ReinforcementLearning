from enums import *
import random

class DungeonSimulator:

    def __init__(self,length=5,slip=0.1,small =2,large=100):
        self.length = length
        self.slip = slip
        self.small = small
        self.large = large
        self.state=0

    def take_action(self,action):
        if random.random() < self.slip:
            action = not action

        if action == BACKWARD :
            reward = self.small
            self.state=0

        elif action == FORWARD :
            if self.state < self.length-1:
                self.state +=1
                reward=0
            else:
                reward=self.large
        return self.state, reward
    
    def reset(self):
        self.state=0
        return self.state


