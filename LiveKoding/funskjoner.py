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
    return avstand

resultat = beregn_avstand(14128, 13948)
print(resultat)

def vurder_tempratur(tempratur):
    if tempratur < -100:
        return "Extremt kaldt"
    elif tempratur < 0:
        return "Kaldt"
    elif tempratur < 30:
        return "varmt og godt"
    else:
        return "ganske brann"

print(vurder_tempratur(24))
print(vurder_tempratur(-24))
print(vurder_tempratur(65))
print(vurder_tempratur(1))
print(vurder_tempratur(-6769))
print(vurder_tempratur(10))
print(vurder_tempratur(3))


def drivstoff_kalkulator_romskip(time, forbrukPrTime):
    return time * forbrukPrTime

print(drivstoff_kalkulator_romskip(1000, 6769))