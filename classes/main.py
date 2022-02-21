# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

from turtle import speed

class Player():
    # Instance method
    def __init__(self, name:str, speed:float, endurance:float, accuracy:float):
        try:
            self.name = name
            self.speed = speed
            self.endurance =  endurance
            self.accuracy = accuracy
        except ValueError:
            print("value should be between 0 and 1")
            
bob = Player("bob", 2, 2, 2)
print(bob.name)