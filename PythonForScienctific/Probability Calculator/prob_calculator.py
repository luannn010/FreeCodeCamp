import copy
import random
# Consider using the modules imported above.
class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        self.get_contents()
        
    
    def get_contents(self):
        for color, ball in self.balls.items():
            self.contents.extend([color] * ball)

    def draw(self,draw_balls):
        drawn_balls = []
        if draw_balls in range(len(self.contents)):
            for i in range(draw_balls):
                # Get the index of the item to be popped
                index = random.randrange(1, len(self.contents) - 1)
                # Pop the item from the list
                ball = self.contents.pop(index)
                drawn_balls.append(ball)
            return  drawn_balls
        return self.contents

            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_contents = hat.contents.copy()  # Create a copy of the hat contents

        # Draw balls from the hat
        drawn_balls = []
        for _ in range(num_balls_drawn):
            if len(hat_contents) == 0:
                break
            random_index = random.randint(0, len(hat_contents) - 1)
            ball = hat_contents.pop(random_index)
            drawn_balls.append(ball)

        # Check if the drawn balls satisfy the expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

