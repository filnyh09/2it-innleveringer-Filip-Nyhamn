# ------------------fra opgave 1-------
class romfartooy:
    def __init__(self, navn, hastighet, drivstoffmengde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde

    def presenter(self):
        return f"\n navn: {self.navn} \n hastighet: {self.hastighet} \n drivstoffmengde: {self.drivstoffmengde} \n"

    def ookeHastigheten(self):
        if (self.drivstoffmengde - 1) >= 0:
            self.hastighet += 1
            self.drivstoffmengde -= 1

# -------------------------------------

class romkargoskip(romfartooy):
    def __init__(self, navn, hastighet, drivstoffmengde, lager):
        super().__init__(navn, hastighet, drivstoffmengde)

        self.lager = lager

    def last(self, mengde):
        self.lager += mengde

    def lever(self):
        self.lager = 0

class rompasasjerskip(romfartooy):
    def __init__(self, navn, hastighet, drivstoffmengde, oksygen, pasasjerer):
        super().__init__(navn, hastighet, drivstoffmengde)

        self.oksygen = oksygen
        self.pasasjerer = pasasjerer

    def landing(self, pasasjererpå, pasasjererav):
        self.oksygen = 100
        self.drivstoffmengde = 5000
        self.pasasjerer += pasasjererpå - pasasjererav

class rommissil(romfartooy):
    def __init__(self, navn, hastighet, drivstoffmengde, mengdedinamit):
        super().__init__(navn, hastighet, drivstoffmengde)

        self.mengdedinamit = mengdedinamit

    def exploder(self):
        return f"booom * {self.mengdedinamit}"

ssromfartooy = rompasasjerskip("ssromfartøy", 10, 50, 68, 12)

romlevrandoor = romkargoskip("rompost", 269, 42, 67)

bigboom = rommissil("bigboom", 9999, 45, 3)

