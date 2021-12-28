# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    result = f"Hi, {name}"
    return result

print(greet('Bob'))

def add(num1, num2, num3):
    result = num1 + num2 + num3
    return result

print(add(5, 3, 2))

def positive(number):
    if number > 0:
        return True
    else:
        return False

print(positive(0))

def negative(number):
    if number < 0:
        return True
    else:
        return False
       
print(negative(-1))