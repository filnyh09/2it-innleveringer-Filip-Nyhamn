Planet0 = "Venus"
Planet1 = "Merkur"
Planet2 = "Jorden"
Planet3 = "Mars"
Planet4 = "Jupiter"
Planet5 = "Saturn"
Planet6 = "Uranus"
Planet7 = "Neptun"

solsystem = [Planet0, Planet1, Planet2, Planet3, Planet4, Planet5, Planet6, Planet7]

print(solsystem)


solsystem.append("Pluto")

print(solsystem)

solsystem.insert(1,"Aries")

print(solsystem)

solsystem.remove("Pluto")

print(solsystem)

solsystem.pop(1)

print(solsystem)

for planet in solsystem:
    if planet == "Venus":
        print(planet, "eksisterer")

solsystem[2] = "Tera"

print(solsystem)

tall = (3, 10, 19)

for tallVerdi in tall:
    print(tallVerdi*2)

for index, planet in enumerate(solsystem):
    print(index, planet)