def satellittmelding(navn, planet):
    print(f"dette er satellitt {navn}")
    print(f"jeg er lokalisert ved {planet}")

def pingSatellitt(avstand):
    return avstand / 300000

def signalTidEstimate(ping):
    if ping < 1:
        print("Direkte kommunikasjon")
    elif ping < 10:
        print("Forsinket kommunikasjon")
    else:
        print("Stor signalforsinkelse")

def Meteorvarsel(diameter, avstandTilJorda):
    if diameter < 67 or avstandTilJorda < 1000:
        return "Lav risiko"
    elif diameter < 





satellittmelding("MESSENGER", "Merkurius")
satellittmelding("Venus Express", "Afrodite")
satellittmelding("Trace Gas Orbiter", "Ares")


satellittping = pingSatellitt(560000)
print(f"signale bruker {satellittping} sekunder for å nå målet.")
signalTidEstimate(satellittping)

satellittping = pingSatellitt(32785248125021303121352062106)
print(f"signale bruker {satellittping} sekunder for å nå målet.")
signalTidEstimate(satellittping)