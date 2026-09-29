from random import randint, choice
from math import sqrt

planetNommer = randint(0,8)

print(planetNommer)

planet = ["mars", "jorda", "jupiter", "VENUS", "saturn", "neptun"]

print(choice(planet))

print(int(sqrt(randint(0,9999999999999))))