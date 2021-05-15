'''
    Python Code to simulate two-block-one-wall system collision.
    The first block has a fixed mass of 1 units, the wall has infinte mass 
    and the mass of second block is of the form 100^(d-1) units.
    All the collisions are elastic.  

    This outputs the toal number of collisions that will take place 
    when the second block is initiated towards the first block, where 
    later is kept stationary in between the second block and the wall.

    We observe from the results that the number of collisions is equal to
    the first d digits of pi.
'''


class Wall:
    def __init__(self, x_c ):
        self.x_c = x_c

'''Class for creating blocks with the method of updating their position after every collision'''
class Block:
    def __init__(self, x_c, velocity, mass):
        self.x_c = x_c
        self.velocity = velocity
        self.mass = mass
    
    def update_position(self, delta_time):
        self.x_c += self.velocity * delta_time

    
'''
    Class that simulates the entire setting.
    Contains methods to initialise and complete the entire state of affairs.

'''

class Frame:

    def __init__(self, block1: Block, block2: Block, wall: Wall):
        self.block1 = block1
        self.block2 = block2
        self.wall = wall
    

    def checkEnded(self):
       if self.block1.velocity >= 0 and self.block2.velocity > 0 and self.block2.velocity > self.block1.velocity:
            return True

    def update_velocity(self):
        temp_v1 = self.block1.velocity
        self.block1.velocity = (((self.block1.mass - self.block2.mass)*self.block1.velocity) + (2*(self.block2.mass)*self.block2.velocity))/(self.block1.mass + self.block2.mass)
        self.block2.velocity = (((self.block2.mass - self.block1.mass)*self.block2.velocity) + (2*(self.block1.mass)*temp_v1))/(self.block1.mass + self.block2.mass)
     


    def update_velocity_b2w(self):
        self.block1.velocity *= -1   
      

    def check_collision(self):

        num_of_collisions = 0


        while True:
            '''finding the time for the next collision of the two blocks and the first block and the wall. '''
            distance = self.block2.x_c - self.block1.x_c
            rel_velocity = self.block2.velocity - self.block1.velocity
            
            if distance == 0:
                timeb2b = 1000
            else:
                timeb2b = abs(distance/rel_velocity)
            if self.block1.velocity == 0:
                timeb2w = 1000
            else:
                timeb2w = abs(self.block1.x_c/self.block1.velocity)



       
            '''Considering all the possible cases of relative motion between two blocks and
            the wall, hence considering all the collisions possible'''

            if self.block1.velocity > 0 and self.block2.velocity > 0 and self.block1.velocity > self.block2.velocity:
                num_of_collisions += 1
                block1.update_position(timeb2b)
                block2.update_position(timeb2b)
                self.update_velocity()
                
                continue
        

            elif self.block1.velocity > 0 and self.block2.velocity < 0:
                num_of_collisions += 1
                block1.update_position(timeb2b)
                block2.update_position(timeb2b)
                self.update_velocity()
                continue
                
            elif self.block1.velocity < 0 and self.block2.velocity > 0:
                num_of_collisions += 1
                block1.update_position(timeb2w)
                block2.update_position(timeb2w)
                self.update_velocity_b2w()
                continue
            
            elif self.block1.velocity < 0 and self.block2.velocity < 0 and self.block2.velocity > self.block1.velocity:
                num_of_collisions += 1
                block1.update_position(timeb2w)
                block2.update_position(timeb2w)
                self.update_velocity_b2w()
                continue 


            elif self.block1.velocity < 0 and self.block2.velocity < 0 and self.block2.velocity < self.block1.velocity:
                if timeb2b < timeb2w:
                    num_of_collisions += 1
                    block1.update_position(timeb2b)
                    block2.update_position(timeb2b)
                    self.update_velocity()
                    continue
            

                else:
                    block1.update_position(timeb2w)
                    block2.update_position(timeb2w)
                    self.update_velocity_b2w()
                    num_of_collisions += 1
                    continue 
            elif self.block1.velocity == 0 and self.block2.velocity < 0 :
                num_of_collisions += 1
                block1.update_position(timeb2b)
                block2.update_position(timeb2b)
                self.update_velocity()
                continue


            elif self.checkEnded() == True:

                print("total numer of collisions:",num_of_collisions)
                break

        return


while True:
    d= int(input("enter the exponenet:"))
    mass1 = 1
    mass2 = 100**(d-1)
    x_c1 = 100
    x_c2 = 200
    x_cw = 0
    v1 = 0
    v2 = -20000
    if mass1 == mass2:
        print("total number of collisions: 3")
    else:
        block1 = Block(x_c1 , v1, mass1)
        block2 = Block(x_c2, v2, mass2)
        wall = Wall(x_cw)

        frame = Frame(block1, block2, wall)

        frame.check_collision()
