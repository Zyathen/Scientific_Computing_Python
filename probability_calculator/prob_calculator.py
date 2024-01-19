import copy
import random
import re
# Consider using the modules imported above.

class Hat:
    # Takes in a dictionary of color of ball and the number of balls in contents
    def __init__(self, **lst_balls):
        self.contents = []
        for color, num in lst_balls.items():
            for _ in range(0, num):
                (self.contents).append(color)
    
    # Draw a num_balls at random and return the list
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        lst_draws = []
        for _ in range(0, num_balls):
            draw = random.randrange(0, len(self.contents))
            lst_draws.append((self.contents).pop(draw))
        return lst_draws    
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    num_successes = 0.00
    # Repeating the experiment num_experiments
    for _ in range(0, num_experiments):
        #Creating a copy of the hat before each draw
        hat_copy = copy.deepcopy(hat)
        actual_balls = hat_copy.draw(num_balls_drawn)

        # Compare the actual balls drawed with expected
        # Count the colors of balls in the actual balls
        actual_balls_sorted = {}
        for color in actual_balls:
            #If the color is one of the exepected balls, update the actual balls dict
            if expected_balls.get(color) != None:
                num_color = actual_balls_sorted.get(color)
                if num_color == None:
                    actual_balls_sorted.update({color : 1})
                else: 
                    actual_balls_sorted.update({color : (num_color + 1)})

        # If the expected balls are present in the actual draw, add one success
        expected = 1
        for color, num in expected_balls.items():
            actual_num = actual_balls_sorted.get(color)
            if actual_num == None or actual_num < num:
               expected = 0
               break
        num_successes += expected

    return num_successes / num_experiments