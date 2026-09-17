def vis_planet(planet, antall_maaner):
    print("-----------")
    print("Velkommen til " + planet)
    print("Antall måner: ", antall_maaner)
    print("-----------")

vis_planet("Mars", 8)
vis_planet("Saturn", 167)
vis_planet("Jord", 1)

def beregn_avstand(fart, timer):
    avstand = fart * timer
    print(avstand)

beregn_avstand(1000, 5)