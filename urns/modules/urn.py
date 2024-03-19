import numpy as np

class urn():
    def __init__(self, length, min=0, max=20):
        self.balls = np.random.randint(min, max, length)
        self.total_ball_weight = np.sum(self.balls)
        self.probability_list = self.balls / self.total_ball_weight
    
    def draw(self):
        draw_index = np.random.randint(0, len(self.balls))
        draw_ball = self.balls[draw_index]
        return draw_index, draw_ball
    
    def add_ball(self, at_this_index):
        self.balls[at_this_index] += 1
        self.total_ball_weight += 1
        self.probability_list = self.balls / self.total_ball_weight
    
    def remove_ball(self, at_this_index):
        self.balls[at_this_index] -= 1
        self.total_ball_weight -= 1
        self.probability_list = self.balls / self.total_ball_weight
    