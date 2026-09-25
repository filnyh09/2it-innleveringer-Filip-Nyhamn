planeter = ["venus", "jorden", "saturn", "mars", "jupiter"]

print(planeter)
print(planeter[0])
print(planeter[-1])

planeter.append("neptun")

print(len(planeter))

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter"]

planeter.remove("Venus")
fjernetPlanet = planeter.pop(2)
print(f"Planeten som ble fjernet var: {fjernetPlanet}")

ekspedisjon = []

for i in range(3):
    ekspedisjon.append(input("hvilke planet ønsker du å besøke?"))

print("Reiseplan:")
for planet in ekspedisjon:
    print(planet)

indre_planeter = ("Merkur", "Venus", "Jorden", "Mars")

print(indre_planeter)
print(indre_planeter[1])

for planet in indre_planeter:
    print(planet)

# jeg får ikkje lov å endre på ein ting ini indre_planeter fordi det er eim tuple