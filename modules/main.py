import this
import time
import math
import datetime
import sys
import greet


# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
def wait(seconds):
    time.sleep(seconds)
    return

def my_sin(float):
    result = math.sin(float)
    return result

def iso_now():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

def platform():
    return sys.platform

def supergreeting_wrapper(name):
    result = greet.supergreeting(name)
    return result


   




##############################
wait(3)
print(my_sin(0.5))
print(iso_now())
print(platform())
print(supergreeting_wrapper("juno"))