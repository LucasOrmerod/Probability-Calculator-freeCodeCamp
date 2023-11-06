import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.contents = []
    self.balls_outside_hat = []
    for k, v in balls.items():
      for _ in range(v):
        self.contents.append(k)

  def draw(self, num):
    if num > len(self.contents):
      self.contents += self.balls_outside_hat
      self.balls_outside_hat = []
      return self.contents

    balls_to_return = []
    for _ in range(num):
      random_ball = random.choice(self.contents)
      self.contents.remove(random_ball)
      self.balls_outside_hat.append(random_ball)
      balls_to_return.append(random_ball)

    return balls_to_return

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_of_matches = 0
    
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    result = hat_copy.draw(num_balls_drawn)
    matches = False
    for k, v in expected_balls.items():
      if result.count(k) >= v:
        matches = True
      else:
        matches = False
        break
        
    if matches:
      num_of_matches += 1
  return num_of_matches / num_experiments