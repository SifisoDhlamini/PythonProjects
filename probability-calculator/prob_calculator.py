import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        else:
            balls_drawn = []
            for i in range(num_balls):
                ball = random.choice(self.contents)
                balls_drawn.append(ball)
                self.contents.remove(ball)
            return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if balls_drawn.count(key) < value:
                break
        else:
            M += 1
    return M / num_experiments

