def satellittmelding(navn, planet):
    print(f"dette er satellitt {navn}")
    print(f"jeg er lokalisert ved {planet}")

def pingSatellitt(avstand):
    return avstand / 300000


satellittmelding("MESSENGER", "Merkurius")
satellittmelding("Venus Express", "Afrodite")
satellittmelding("Trace Gas Orbiter", "Ares")

print(f"signale bruker {pingSatellitt(560000)} sekunder for å nå målet.")
print(f"signale bruker {pingSatellitt(32785248125021303121352062106)} sekunder for å nå målet.")