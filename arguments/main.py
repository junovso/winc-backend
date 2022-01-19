# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greet_template="Hello, <name>!"):
    good_greet = greet_template.replace("<name>",name)
    return (good_greet)

print(greet('juno', "whatdap <name>"))

def force(mass: float, body="earth"):
    celestial_bodies = {
        "Sun": 274,
        "Jupiter": 24.92,
        "Neptune": 11.15,
        "Saturn": 10.44,
        "Earth": 9.798,
        "Uranus": 8.87,
        "Venus": 8.87,
        "Mars": 3.71,
        "Mercury": 3.7,
        "Moon": 1.62,
        "Pluto": 0.58,
    }
    mass = float(mass)
    surface_gravity = celestial_bodies[body.lower().capitalize()]
    surface_gravity_rounded = round(float(surface_gravity), 1)
    gravity = surface_gravity_rounded
    force_newton = mass * gravity
    return force_newton


 # Exercise 3

def pull(m1= "float in kg", m2= "float in kg", d= "distance"):
    g = 6.674 * 10 ** -11
    gravitational_pull = g * ((m1 * m2) / (d ** 2))
    return gravitational_pull

print(pull(2,3,10))