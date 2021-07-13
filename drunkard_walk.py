import random
import subprocess

subprocess.call(['clear'])

'''class to execute a fair toss'''
class Coin:
    def __init__(self):
        pass

    @staticmethod
    def toss():
        outcome = random.uniform(0,1)
        if outcome < 0.5:
            return "heads"
        else:
            return "tails"


'''drunkard to assign its position of house and x_coordinate'''

class Drunkard:
    def __init__(self, x_c, house_at):
        self.x_c = x_c
        self.house_at = house_at



'''
    Simulation the walk of drunkard with two base case:
        -to always move right at the origin
        -terminate when drunkard reaches house position
    while at any other x_coordinate, the next step direction 
    is determined on the basis of a fair toss with unifom 
    distribution.
'''
class Simulator:
    def __init__(self, drunkard :Drunkard, coin : Coin):
        self.drunkard = drunkard
        self.coin = coin

    def count_steps(self):
        steps_walked = 0

        while True:
            if self.drunkard.x_c == self.drunkard.house_at:
                break
            
            steps_walked += 1

            if self.drunkard.x_c == 0:
                self.drunkard.x_c += 1
                continue

            else:
                toss = self.coin.toss()
                if toss == "heads":
                    self.drunkard.x_c += 1
                else:
                    self.drunkard.x_c -= 1


        return steps_walked



'''
    main:
    to analyse the nature of result, we perform the simulation
    large number of times(100 here) for the same house position and 
    take the average of the individual results. It is observed that 
    the average steps is equal to the square of house position.
'''
house_pos = [10, 50, 100, 200]
for hpos in house_pos:

    avg_steps = 0
    num_trials = 100

    
    for _ in range(num_trials):
        
        coin = Coin()
        drunkard = Drunkard(0, hpos)
        simulation =  Simulator(drunkard , coin)
        curr_steps = simulation.count_steps()
        avg_steps += curr_steps
        

    avg_steps /= num_trials

    print(f'HPOS: {hpos}, steps required : {avg_steps}')